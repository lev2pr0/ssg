import unittest

from textnode import TextNode, TextType
from split_textnode import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.duh.com")
        node2 = TextNode("This is a crazy text node", TextType.LINK, "google.com")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_type(self):
        node = TextNode("This is text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_codesplit(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_boldsplit(self):
        node = TextNode("This is text with a **BOLD text** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("BOLD text", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_italicsplit(self):
        node = TextNode("This is text with a _Italics text_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("Italics text", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_split_noclose(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is text with a _Random text word", TextType.TEXT)
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_split_unknown(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is text with a ++Random text word++", TextType.TEXT)
            split_nodes_delimiter([node], "++", TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()
