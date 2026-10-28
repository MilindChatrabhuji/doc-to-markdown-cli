from doc_to_markdown import html_to_markdown

def test_html_conversion():
    html = "<h1>Welcome</h1><p>This is a paragraph.</p><ul><li>First item</li><li>Second item</li></ul>"
    md = html_to_markdown(html)
    assert "# Welcome" in md
    assert "This is a paragraph." in md
    assert "- First item" in md
