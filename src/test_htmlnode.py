import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev", "target": "_blank"})
        node2 = HTMLNode("a", "link", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev", "target": "_blank"})
        node2 = HTMLNode("a", "boot", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(a, link, None, {'href': 'https://www.boot.dev', 'target': '_blank'})")
        
    def test_props(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"  target="_blank"')

if __name__ == "__main__":
    unittest.main()