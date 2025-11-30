def summarize_text(text: str, mode: str='short'):
    """Simple rule-based summarizer placeholder.
    For hackathon use, replace with an LLM or transformer-based summarizer.
    """
    # naive approach: split into sentences and pick first N
    import re
    sents = re.split(r'(?<=[.!?])\s+', text.strip())
    n = 5 if mode=='short' else 15
    summary = '\n'.join(sents[:n])
    # post-process to bullets
    bullets = '\n'.join(['- ' + s.strip() for s in summary.split('\n') if s.strip()])
    return bullets
