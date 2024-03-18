from textnode import TextNode, text_node_to_html_node

def main():
    tn1 = TextNode("This is a bold node", "bold")
    tn2 = TextNode("This is an italic node", "italic")
    tn3 = TextNode("This is a code node", "code")
    tn4 = TextNode("This is a link node", "link", "https://www.boot.dev")
    tn5 = TextNode("This is an image node", "image", "test.png")
    tn6 = TextNode("This is a text node", "text")

    print(text_node_to_html_node(tn1))
    print(text_node_to_html_node(tn2))
    print(text_node_to_html_node(tn3))
    print(text_node_to_html_node(tn4))
    print(text_node_to_html_node(tn5))
    print(text_node_to_html_node(tn6))

    hn1 = text_node_to_html_node(tn1)
    hn2 = text_node_to_html_node(tn2)
    hn3 = text_node_to_html_node(tn3)
    hn4 = text_node_to_html_node(tn4)
    hn5 = text_node_to_html_node(tn5)
    hn6 = text_node_to_html_node(tn6)

    print(hn1.to_html())
    print(hn2.to_html())
    print(hn3.to_html())
    print(hn4.to_html())
    print(hn5.to_html())
    print(hn6.to_html())
    
    
if __name__ == "__main__":
    main()