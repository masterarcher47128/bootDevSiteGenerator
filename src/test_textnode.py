import unittest
import requests

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_blank(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("testing the URL", TextType.LINK, "https://www.boot.dev")
        if node.url:
            response = requests.get(node.url)
            self.assertEqual(response.status_code, 200, f"URL {node.url} is not reachable")
        else:
            self.fail("URL is None or empty")
    
    def test_repr(self):
        node = TextNode("Sample text", TextType.BOLD, "https://example.com")
        self.assertEqual(repr(node), "TextNode(Sample text, bold, https://example.com)")

    def test_neq_different_urls(self):
        node1 = TextNode("Sample text", TextType.LINK, "https://example1.com")
        node2 = TextNode("Sample text", TextType.LINK, "https://example2.com")
        self.assertNotEqual(node1, node2)

    def test_empty_url(self):
        node = TextNode("Sample text", TextType.LINK, None)
        self.assertIsNone(node.url)

    def test_neq_different_text_types(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_default_url(self):
        node = TextNode("Sample text", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        self.assertEqual(node.text, "")

    def test_long_text(self):
        long_text = "a" * 10000  # 10,000 characters
        node = TextNode(long_text, TextType.TEXT)
        self.assertEqual(node.text, long_text)

    def test_comparison_with_non_textnode(self):
        node = TextNode("Sample text", TextType.BOLD)
        self.assertNotEqual(node, "Not a TextNode")

    def test_case_sensitivity(self):
        node1 = TextNode("Sample Text", TextType.TEXT)
        node2 = TextNode("sample text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()