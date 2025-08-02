import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        print(f'\nTest None\n==========\nNode 1: {node}\n\nNode 2: {node2}')
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

if __name__ == "__main__":
    unittest.main()
