import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links
from block_markdown import markdown_to_blocks
from blocktype import BlockType, block_to_block_type

class TestMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

   # def test_blocktype_heading(self):

   # def test_blocktype_code(self):

   # def test_blocktype_quote(self):

   # def test_blocktype_unordered_list(self):

    def test_blocktype_ordered_list(self):
        block = """
1. This is an ordered list
2. with items
"""
        blocktype = block_to_block_type(block)
        print(f"result = {blocktype}")
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)

  #  def test_sequential_error(self):

  # def test_number_error(self):

  # def test_blocktype_ordered_list(self):

  # def test_blocktype_paragraph(self):
