from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        ) 

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href": self.url})
        elif self.text_type == TextType.IMAGE:
            return LeafNode("img", None, {"src": self.url, "alt": self.text})
        elif self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        elif self.text_type == TextType.BOLD:
            return LeafNode("strong", self.text)
        elif self.text_type == TextType.ITALIC:
            return LeafNode("em", self.text)
        elif self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        else:
            raise Exception("Invalid text type")  # This should never happen
