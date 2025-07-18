# library/reader.py

import pikepdf
from .catalog import list_ebooks

def read_pdf(file_path):
    """Read and print the content of a PDF eBook."""
    try:
        with pikepdf.open(file_path) as pdf:
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                print(page.extract_text())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def read_all_ebooks():
    """Read and print content of all eBooks."""
    ebooks = list_ebooks()
    for ebook in ebooks:
        print(f"Reading {ebook}...")
        read_pdf(ebook)
