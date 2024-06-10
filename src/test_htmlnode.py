import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_children(self):
        node_p = HTMLNode("p", "This is a paragraph")
        node_div = HTMLNode(
            "div", "Inside the DIV", node_p, {"class": "red", "id": "my_div"}
        )

        self.assertEqual(node_div.props_to_html(), ' class="red" id="my_div"')


if __name__ == "__main__":
    unittest.main()
