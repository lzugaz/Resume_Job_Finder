from PyPDF2 import PdfReader as PDFReader
import re

def pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PDFReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    
    return text


