from leafnode import LeafNode
from enum import Enum


class TextNode:
    """
    A "TextNode" is sort of an intermediate representation between
    Markdown and HTML, and is specific to inline markup.
    It includes Normal text, Bold, Italic, Code, Links and Images.

    Attributes
    ----------
    text : str
        a string
    text_type : str
        blabla
    url : str
        blabla

    Methods
    -------

    """

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT.value:
            return LeafNode(self.text)
        if self.text_type == TextType.BOLD.value:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC.value:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE.value:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK.value:
            return LeafNode("a", self.text, {"href": self.url})
        if self.text_type == TextType.IMAGE.value:
            return LeafNode("img", "", {"src": self.url, "alt": self.text})

        raise Exception("TextNode Class: text_type not valid")


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextTypeDelimiter(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"
