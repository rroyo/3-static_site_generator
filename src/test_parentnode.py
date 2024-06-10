import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_inner_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode("code", "Code snippet"),
                ParentNode(
                    "div",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "Italic text"),
                        LeafNode("code", "Code snippet"),
                    ],
                ),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i><code>Code snippet</code><div><b>Bold text</b>Normal text<i>Italic text</i><code>Code snippet</code></div></p>",
        )
