import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode


class TestHTMLNode(unittest.TestCase):

    def test_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertIsNot(node, node2)

    def test_eq(self):
        node = HTMLNode(tag="h1",value="Title",children=[HTMLNode(tag="p", value="Paragraph")],props={"class": "title"})
        node2 = HTMLNode(tag="h1",value="Title",children=[HTMLNode(tag="p", value="Paragraph")],props={"class": "title"})
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HTMLNode(
            tag="h1",
            value="Title",
            children=[HTMLNode(tag="p", value="Paragraph")],
            props={"class": "title"}
        )
        node2 = HTMLNode(
            tag="h1",
            value="FooTitle",
            props={"class": "title"}
        )
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_value_none(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_tag_none(self):
        node = LeafNode(None, "Raw Text")
        self.assertEqual(node.to_html(), "Raw Text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_child(self):
        node = ParentNode("div", None)
        self.assertRaises(ValueError, node.to_html)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is an anchor text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is an anchor text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("This is an alt text node", TextType.IMAGE, "https://stock.adobe.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {
            "src": "https://stock.adobe.com",
            "alt": "This is an alt text node"
            }
        )

    def test_texttype_none(self):
        node = TextNode("This is a text node", None)
        self.assertRaises(ValueError, text_node_to_html_node, node)

if __name__ == "__main__":
    unittest.main()
