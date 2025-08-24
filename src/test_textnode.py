import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode(
            "This is text with no link or images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no link or images", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode(
            "This is text with no link or images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no link or images", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()
