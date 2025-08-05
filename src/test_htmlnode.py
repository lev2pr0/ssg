import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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



if __name__ == "__main__":
    unittest.main()
