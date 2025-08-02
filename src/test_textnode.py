import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        node2 = TextNode("This is a plain text node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_eq(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        node2 = TextNode("This is a italic text node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_eq(self):
        node = TextNode("This is a code text node", TextType.CODE)
        node2 = TextNode("This is a code text node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq(self):
        node = TextNode("This is a link text node", TextType.LINK)
        node2 = TextNode("This is a link text node", TextType.LINK)
        self.assertEqual(node, node2)
    
    def test_eq(self):
        node = TextNode("This is a image text node", TextType.IMAGE)
        node2 = TextNode("This is a image text node", TextType.IMAGE)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a plain text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a link", TextType.LINK, url="https://github.com/alivia-g/site-generator")
        node2 = TextNode("This is a link", TextType.LINK, url="https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1")
        self.assertNotEqual(node, node2)
    
    def test_url_not_eq_2(self):
        node = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK, url="https://github.com/alivia-g/site-generator")
        self.assertNotEqual(node, node2)
    
    def test_text_type_not_eq(self):
        node = TextNode("This is an image", TextType.IMAGE)
        node2 = TextNode("This is a code text", TextType.CODE)
        self.assertNotEqual(node, node2)

class TestTextNodetoHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://github.com/alivia-g/site-generator")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://github.com/alivia-g/site-generator", "alt": "This is an image"},
        )
    
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()