import unittest

import textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = textnode.TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = textnode.TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = textnode.TextNode("This is a text node", "bold")
        node2 = textnode.TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_type_different(self):
        node = textnode.TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = textnode.TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = textnode.TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.boot.dev)")
    
    def test_delim_bold(self):
        node = textnode.TextNode("This is text with a **bolded** word", textnode.text_type_text)
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.text_type_bold)
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.text_type_text),
                textnode.TextNode("bolded", textnode.text_type_bold),
                textnode.TextNode(" word", textnode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = textnode.TextNode(
            "This is text with a **bolded** word and **another**", textnode.text_type_text
        )
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.text_type_bold)
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.text_type_text),
                textnode.TextNode("bolded", textnode.text_type_bold),
                textnode.TextNode(" word and ", textnode.text_type_text),
                textnode.TextNode("another", textnode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = textnode.TextNode(
            "This is text with a **bolded word** and **another**", textnode.text_type_text
        )
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.text_type_bold)
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.text_type_text),
                textnode.TextNode("bolded word", textnode.text_type_bold),
                textnode.TextNode(" and ", textnode.text_type_text),
                textnode.TextNode("another", textnode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = textnode.TextNode("This is text with an *italic* word", textnode.text_type_text)
        new_nodes = textnode.split_nodes_delimiter([node], "*", textnode.text_type_italic)
        self.assertListEqual(
            [
                textnode.TextNode("This is text with an ", textnode.text_type_text),
                textnode.TextNode("italic", textnode.text_type_italic),
                textnode.TextNode(" word", textnode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = textnode.TextNode("This is text with a `code block` word", textnode.text_type_text)
        new_nodes = textnode.split_nodes_delimiter([node], "`", textnode.text_type_code)
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.text_type_text),
                textnode.TextNode("code block", textnode.text_type_code),
                textnode.TextNode(" word", textnode.text_type_text),
            ],
            new_nodes,
        )
    
    def test_markdown_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        extracted = textnode.extract_markdown_images(text)
        self.assertEqual(extracted, [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def text_markdown_links(self):
        text = "This is text with a [link](https://www.boot.dev) and [another](https://www.exmple.com)"
        extracted = textnode.extract_markdown_links(text)
        self.assertEqual(extracted, [("link", "https://www.boot.dev"), ("another", "https://www.example.com")])

if __name__ == "__main__":
    unittest.main()