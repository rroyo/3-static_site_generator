# This class will handle the nesting of HTML nodes inside of one another.
# Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.

from htmlnode import HTMLNode
from textnode import TextNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required")

        if not self.children:
            raise ValueError("children is required")

        node = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            if type(child) == TextNode:
                node += child.text_node_to_html_node().to_html()
            else:
                node += child.to_html()

        return f"{node}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
