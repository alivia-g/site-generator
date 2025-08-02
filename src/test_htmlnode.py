import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        my_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        html_node = HTMLNode(props=my_props)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', html_node.props_to_html()
        )
    
    def test_nodes_eq(self):
        node = HTMLNode("p", "this is a text", None, None)
        node2 = HTMLNode("p", "this is a text", None, None)
        self.assertEqual(node, node2)
    
    def test_nodes_not_eq(self):
        node = HTMLNode("p", "this is a text", None, None)
        node2 = HTMLNode("a", "this is a text", None, None)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "tag: p, value: What a strange world, children: None, props: {'class': 'primary'}"
        )