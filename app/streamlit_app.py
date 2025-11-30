import streamlit as st
from app.pdf_extractor import extract_text_from_pdf
from app.summarizer import summarize_text
from app.mcq_generator import generate_mcqs
from app.utils import download_button

st.set_page_config(page_title='Adaptive MCQ & Notes', layout='wide')
st.title('Adaptive MCQ & Notes Generator — Demo')

uploaded = st.file_uploader('Upload a PDF chapter', type=['pdf'])
text_input = st.text_area('Or paste text here', height=200)

difficulty = st.selectbox('Select difficulty', ['Mixed', 'Easy', 'Medium', 'Hard'])
col1, col2 = st.columns(2)
if col1.button('Generate Notes'):
    if uploaded:
        text = extract_text_from_pdf(uploaded)
    else:
        text = text_input
    if not text:
        st.error('No text provided.')
    else:
        notes = summarize_text(text, mode='short')
        st.markdown('### Generated Notes')
        st.write(notes)
        download_button(notes, 'notes.md', 'Download Notes')

if col2.button('Generate MCQs'):
    if uploaded:
        text = extract_text_from_pdf(uploaded)
    else:
        text = text_input
    if not text:
        st.error('No text provided.')
    else:
        mcqs = generate_mcqs(text, n=10, difficulty=difficulty)
        st.markdown('### Generated MCQs')
        for i, q in enumerate(mcqs, 1):
            st.write(f"**Q{i}. {q['question']}**")
            for idx, opt in enumerate(q['options'], ord('A')):
                st.write(f"{chr(idx)}. {opt}")
            st.write(f"**Answer:** {q['answer']} — *{q['difficulty']}*" )
            st.write('---')
        import csv, io
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(['question','options','answer','difficulty'])
        for q in mcqs:
            writer.writerow([q['question'], ' || '.join(q['options']), q['answer'], q['difficulty']])
        download_button(buf.getvalue(), 'mcqs.csv', 'Download MCQs')
