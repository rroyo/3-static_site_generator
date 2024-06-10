import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD.value)
        node2 = TextNode("This is a text node", TextType.BOLD.value)
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD.value)
        node2 = TextNode(
            "This is a text node", TextType.BOLD.value, "https://google.com"
        )
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode(
            "This is a boring text node", TextType.BOLD.value, "https://google.com"
        )
        node2 = TextNode(
            "This is a text node", TextType.BOLD.value, "https://google.com"
        )
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode(
            "This is a text node", TextType.ITALIC.value, "https://google.com"
        )
        node2 = TextNode(
            "This is a text node", TextType.BOLD.value, "https://google.com"
        )
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node = TextNode(
            "This is a text node", TextType.ITALIC.value, "https://google.com"
        )
        self.assertEqual(type(node.text_node_to_html_node()), LeafNode)


if __name__ == "__main__":
    unittest.main()
