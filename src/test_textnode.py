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



if __name__ == "__main__":
    unittest.main()