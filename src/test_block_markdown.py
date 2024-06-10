import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items
"""
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph\nNo fancy Markdown\nJust 3 lines of text"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_type_heading_1(self):
        block = "# This is a level 1 heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_heading_3(self):
        block = "### This is a level 3 heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_heading_6(self):
        block = "### This is a level 6 heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_code(self):
        block = "```Multiline code\nSecond Line of code\nThird line of code```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_quote(self):
        block = (
            ">First line of the quotes\n> Second line of quotes\n>Third line of quotes"
        )
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_unordered_list(self):
        block = "* Unordered item 1\n- Unordered item 2\n- Unordered item 3"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Ordered item 1\n2. Ordered item 2\n3. Ordered item 3"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
