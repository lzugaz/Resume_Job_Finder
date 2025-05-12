from PyPDF2 import PdfReader as PDFReader
import re

def pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PDFReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    clean_resume_text(text)
    return text


def clean_resume_text(text):
    # Fix split hyphenated words (e.g., "learn-\ning" → "learning")
    text = re.sub(r'-\n', '')
    
    # Replace remaining newlines with space, but only if they’re not at the end of a sentence
    text = re.sub(r'(?<![.\n])\n(?!\n)', ' ', text)

    # Collapse multiple spaces
    text = re.sub(r'\s{2,}', ' ', text)

    return text.strip()