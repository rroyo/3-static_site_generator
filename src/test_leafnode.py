import unittest

from leafnode import LeafNode


class TestLeadNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", {"class": "p_tag"})
        print(node.to_html())

    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None).to_html()

    def test_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        print(node.to_html())


if __name__ == "__main__":
    unittest.main()
