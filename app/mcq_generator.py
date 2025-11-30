import random
import re

def simple_question_from_sentence(sent):
    # naive question generator: replace a noun phrase with a blank
    # For demo purposes, create a placeholder question.
    q = sent.strip()
    if len(q) < 20:
        q = q + ' (Explain)'
    # create options
    options = [q[:min(30,len(q))] + ' ...', 'Distractor 1', 'Distractor 2', 'Distractor 3']
    random.shuffle(options)
    return {'question': q, 'options': options, 'answer': options[0], 'difficulty': 'Medium'}

def generate_mcqs(text: str, n: int=10, difficulty: str='Mixed'):
    import re
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    out = []
    i = 0
    for sent in sents:
        if i>=n: break
        if len(sent) > 40:
            out.append(simple_question_from_sentence(sent))
            i += 1
    # pad if needed
    while len(out) < n:
        out.append({'question': f'Placeholder question {len(out)+1}', 'options': ['A','B','C','D'], 'answer':'A', 'difficulty': difficulty})
    return out
