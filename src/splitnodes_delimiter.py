from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            splitted_chunks = node.text.split(delimiter)
            if len(splitted_chunks) % 2 == 0:
                raise Exception("Unmatched delimiter in text")
            for i in range(0, len(splitted_chunks)):
                if splitted_chunks[i] != "":    
                    if i % 2 == 0:
                        new_nodes.append(TextNode(splitted_chunks[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(splitted_chunks[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes