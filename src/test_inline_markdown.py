import unittest
from textnode import TextNode, TextType, TextTypeDelimiter
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT.value)

        self.assertEqual(
            split_nodes_delimiter(
                [node], TextTypeDelimiter.CODE.value, TextType.CODE.value
            ),
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" word", TextType.TEXT.value),
            ],
        )

    def test_split_nodes_delimiter_code_multiple_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT.value)
        node2 = TextNode(
            "This is text with another `code block` word", TextType.TEXT.value
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node, node2], TextTypeDelimiter.CODE.value, TextType.CODE.value
            ),
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" word", TextType.TEXT.value),
                TextNode("This is text with another ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" word", TextType.TEXT.value),
            ],
        )

    def test_split_nodes_delimiter_code_multiword(self):
        node = TextNode(
            "This is text with a `code block` word here and another `code block` here",
            TextType.TEXT.value,
        )

        self.assertEqual(
            split_nodes_delimiter(
                [node], TextTypeDelimiter.CODE.value, TextType.CODE.value
            ),
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" word here and another ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" here", TextType.TEXT.value),
            ],
        )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertTrue(
            extract_markdown_images(text),
            [
                (
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                (
                    "another",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
                ),
            ],
        )

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )

    def test_split_nodes_image_multiple_nodes(self):
        node1 = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT.value,
        )
        node2 = TextNode(
            "This is text with another ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and yet another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT.value,
        )
        self.assertEqual(
            split_nodes_image([node1, node2]),
            [
                TextNode("This is text with an ", TextType.TEXT.value),
                TextNode(
                    "image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT.value),
                TextNode(
                    "second image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
                TextNode("This is text with another ", TextType.TEXT.value),
                TextNode(
                    "image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and yet another ", TextType.TEXT.value),
                TextNode(
                    "second image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_split_nodes_image_ending_text(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and a last text.",
            TextType.TEXT.value,
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", TextType.TEXT.value),
                TextNode(
                    "image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT.value),
                TextNode(
                    "second image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
                TextNode(" and a last text.", TextType.TEXT.value),
            ],
        )

    def test_split_nodes_link_multiple_nodes(self):
        node1 = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT.value,
        )
        node2 = TextNode(
            "This is text with another [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and yet another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT.value,
        )
        self.assertEqual(
            split_nodes_link([node1, node2]),
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode(
                    "link",
                    TextType.LINK.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT.value),
                TextNode(
                    "second link",
                    TextType.LINK.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
                TextNode("This is text with another ", TextType.TEXT.value),
                TextNode(
                    "link",
                    TextType.LINK.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and yet another ", TextType.TEXT.value),
                TextNode(
                    "second link",
                    TextType.LINK.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_split_nodes_link_ending_text(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and a last text.",
            TextType.TEXT.value,
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with a ", TextType.TEXT.value),
                TextNode(
                    "link",
                    TextType.LINK.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT.value),
                TextNode(
                    "second link",
                    TextType.LINK.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
                TextNode(" and a last text.", TextType.TEXT.value),
            ],
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT.value),
                TextNode("text", TextType.BOLD.value),
                TextNode(" with an ", TextType.TEXT.value),
                TextNode("italic", TextType.ITALIC.value),
                TextNode(" word and a ", TextType.TEXT.value),
                TextNode("code block", TextType.CODE.value),
                TextNode(" and an ", TextType.TEXT.value),
                TextNode(
                    "image",
                    TextType.IMAGE.value,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and a ", TextType.TEXT.value),
                TextNode("link", TextType.LINK.value, "https://boot.dev"),
            ],
        )
