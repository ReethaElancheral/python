# library/__init__.py

from .catalog import list_ebooks, get_metadata
from .search import search_ebooks
from .reader import read_pdf, read_all_ebooks

__all__ = ['list_ebooks', 'get_metadata', 'search_ebooks', 'read_pdf', 'read_all_ebooks']
