class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def __eq__(self, __value: object) -> bool:
        return self.tag == __value.tag and self.value == __value.value and self.children == __value.children and self.props == __value.props