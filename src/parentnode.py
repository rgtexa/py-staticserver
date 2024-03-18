from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if self.children is None:
            raise ValueError("children cannot be None")
        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"