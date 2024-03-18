import leafnode
class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, __value: object) -> bool:
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "bold":
            return leafnode.LeafNode("b", text_node.text)
        case "italic":
            return leafnode.LeafNode("i", text_node.text)
        case "code":
            return leafnode.LeafNode("code", text_node.text)
        case "link":
            return leafnode.LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return leafnode.LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case "text":
            return leafnode.LeafNode(None, text_node.text)
        case _:
            raise ValueError(f"Unknown text type: {text_node.text_type}")