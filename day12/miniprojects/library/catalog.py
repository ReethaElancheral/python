# library/catalog.py

import glob
import os
import pikepdf
from .config import BOOKS_DIRECTORY, SUPPORTED_FORMATS

def list_ebooks():
    """List all eBooks in the specified directory."""
    ebooks = []
    for ext in SUPPORTED_FORMATS:
        ebooks.extend(glob.glob(os.path.join(BOOKS_DIRECTORY, '*' + ext)))
    return ebooks

def get_metadata(file_path):
    """Retrieve metadata for a PDF eBook."""
    try:
        with pikepdf.open(file_path) as pdf:
            metadata = pdf.docinfo
            return {
                'title': metadata.get('/Title', 'Unknown Title'),
                'author': metadata.get('/Author', 'Unknown Author'),
                'subject': metadata.get('/Subject', 'Unknown Subject'),
                'producer': metadata.get('/Producer', 'Unknown Producer'),
                'created': metadata.get('/CreationDate', 'Unknown Date')
            }
    except Exception as e:
        print(f"Error reading metadata from {file_path}: {e}")
        return {}
