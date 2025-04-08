import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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



class TestLeafNode(unittest.TestCase):
    def test_to_html_with_value_and_tag(self):
        leaf = LeafNode("span", "Hello, World!", {"class": "highlight"})
        self.assertEqual(
            leaf.to_html(),
            '<span class= highlight >Hello, World!</span>'
        )

    def test_to_html_without_value(self):
        leaf = LeafNode("span", None, {"class": "highlight"})
        with self.assertRaises(ValueError):
            leaf.to_html()

    def test_to_html_without_tag(self):
        leaf = LeafNode(None, "Hello, World!")
        self.assertEqual(leaf.to_html(), "Hello, World!")

    def test_props_to_html(self):
        leaf = LeafNode("img", None, {"src": "image.png", "alt": "An image"})
        self.assertEqual(
            leaf.props_to_html(),
            ' src= image.png  alt= An image '
        )

    def test_repr(self):
        leaf = LeafNode("img", "Image", {"src": "image.png"})
        self.assertEqual(
            repr(leaf),
            "LeafNode(tag: img, value: Image, children: None, properties: {'src': 'image.png'})"
        )

    def test_empty_props(self):
        leaf = LeafNode("div", "Content", {})
        self.assertEqual(leaf.props_to_html(), "")

    def test_to_html_with_empty_props(self):
        leaf = LeafNode("div", "Content", {})
        self.assertEqual(leaf.to_html(), "<div>Content</div>")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_tag_and_children(self):
        child1 = LeafNode("span", "Child 1")
        child2 = LeafNode("span", "Child 2")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            '<div><span>Child 1</span><span>Child 2</span></div>'
        )

    def test_to_html_without_tag(self):
        child = LeafNode("span", "Child")
        parent = ParentNode(None, None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_without_children(self):
        parent = ParentNode("div", None, [])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
