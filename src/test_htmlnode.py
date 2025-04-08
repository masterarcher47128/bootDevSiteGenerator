import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",       
        }
        htmlNode = HTMLNode("a", "link", None, test_props)
        self.assertEqual(htmlNode.props_to_html(), ' href= https://www.google.com  target= _blank ')

    def test_repr(self):
        htmlNode = HTMLNode("div", "content", None, {"class": "container"})
        self.assertEqual(
            repr(htmlNode),
            "HTMLNode(tag: div, value: content, children: None, properties: {'class': 'container'})"
        )

    def test_empty_node(self):
        htmlNode = HTMLNode()
        self.assertEqual(htmlNode.tag, None)
        self.assertEqual(htmlNode.value, None)
        self.assertEqual(htmlNode.children, None)
        self.assertEqual(htmlNode.props, None)

    def test_to_html_not_implemented(self):
        htmlNode = HTMLNode("p", "text")
        with self.assertRaises(NotImplementedError):
            htmlNode.to_html()

    def test_children(self):
        child1 = HTMLNode("span", "child1")
        child2 = HTMLNode("span", "child2")
        parent = HTMLNode("div", None, [child1, child2])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].tag, "span")
        self.assertEqual(parent.children[1].value, "child2")