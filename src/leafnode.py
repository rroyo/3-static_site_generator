# A LeafNode is a type of HTMLNode that represents a single HTML tag with no children.
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
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

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is required")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
