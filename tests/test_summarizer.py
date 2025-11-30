from app.summarizer import summarize_text
def test_summarize():
    text = 'This is sentence one. This is sentence two. This is sentence three.'
    s = summarize_text(text, mode='short')
    assert '- This is sentence one.' in s
