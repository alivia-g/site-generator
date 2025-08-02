from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is None")
        if self.children is None:
            raise ValueError("Children is None")
        # open tag
        rslt = f'<{self.tag}>'
        for c in self.children:
            rslt += c.to_html()
        rslt += f'</{self.tag}>'
        return rslt
        