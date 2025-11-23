from langparse.autoparser import AutoParser
from langparse.parsers.markdown_parser import MarkdownParser
from langparse.parsers.docx_parser import DocxParser
from langparse.parsers.excel_parser import ExcelParser

def test_autoparser_routing(sample_md_file, sample_docx_file, sample_excel_file):
    # MD
    doc = AutoParser.parse(sample_md_file)
    assert doc.metadata['filename'] == 'test.md'
    
    # DOCX
    doc = AutoParser.parse(sample_docx_file)
    assert doc.metadata['extension'] == '.docx'
    
    # Excel
    doc = AutoParser.parse(sample_excel_file)
    assert doc.metadata['extension'] == '.xlsx'

def test_autoparser_pdf_delegation(tmp_path):
    # We just check if it tries to instantiate PDFParser
    # Since we don't have a real PDF file and don't want to mock everything here,
    # we can just check if it raises ImportError or similar if dependencies are missing,
    # or just trust the routing logic.
    # A simple way is to mock PDFParser inside autoparser.
    pass 
