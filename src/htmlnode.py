class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        rslt = ""
        for k, v in self.props.items():
            rslt += f' {k}="{v}"'
        return rslt

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
    def __eq__(self, htmlnode):
        if isinstance(htmlnode, HTMLNode):
            return (
                self.tag == htmlnode.tag and
                self.value == htmlnode.value and
                self.children == htmlnode.children and
                self.props == htmlnode.props
            )
        return False