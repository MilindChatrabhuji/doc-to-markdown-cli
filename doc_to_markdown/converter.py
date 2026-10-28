import re
from html.parser import HTMLParser

class HTMLToMarkdownParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in ["h1", "h2", "h3"]:
            level = int(tag[1])
            self.output.append("\n" + ("#" * level) + " ")
        elif tag == "p":
            self.output.append("\n\n")
        elif tag == "li":
            self.output.append("\n- ")

    def handle_data(self, data):
        self.output.append(data)

def html_to_markdown(html_content: str) -> str:
    parser = HTMLToMarkdownParser()
    parser.feed(html_content)
    raw = "".join(parser.output)
    return clean_text_for_llm(raw)

def clean_text_for_llm(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
