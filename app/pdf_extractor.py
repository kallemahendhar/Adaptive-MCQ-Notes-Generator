import pdfplumber

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file uploaded via Streamlit."""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            pages = [p.extract_text() or '' for p in pdf.pages]
        return '\n'.join(pages)
    except Exception as e:
        # fallback: try read .read()
        try:
            uploaded_file.seek(0)
            raw = uploaded_file.read().decode('utf-8', errors='ignore')
            return raw
        except Exception:
            return ''
