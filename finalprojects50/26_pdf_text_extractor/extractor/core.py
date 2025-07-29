import PyPDF2

def extract_text(pdf_path):
    """
    Generator to yield text page-by-page from the PDF.
    Handles encrypted PDFs by attempting to decrypt with empty password.
    """
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            if reader.is_encrypted:
                try:
                    reader.decrypt("")
                except Exception:
                    raise ValueError("PDF is encrypted and cannot be decrypted.")

            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    cleaned_text = text.strip().replace('\n', ' ')
                    yield cleaned_text
                else:
                    yield "[No text found on this page]"
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{pdf_path}' not found.")
