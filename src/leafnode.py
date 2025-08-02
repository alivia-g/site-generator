from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node has no value")
        if self.tag is None:
            return self.value
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        # get props into html
        propstring = ""
        for k, v in self.props.items():
            propstring += f' {k}="{v}"'
        return f'<{self.tag}{propstring}>{self.value}</{self.tag}>'