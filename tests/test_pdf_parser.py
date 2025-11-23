from unittest.mock import MagicMock, patch
from langparse.parsers.pdf_parser import PDFParser
from langparse.engines.pdf.simple import SimplePDFEngine
from langparse.core.engine import PageResult

def test_pdf_parser_simple_engine_flow():
    # Mock the SimplePDFEngine.process method
    with patch('langparse.engines.pdf.simple.SimplePDFEngine.process') as mock_process:
        # Setup mock return values
        mock_process.return_value = iter([
            PageResult(page_number=1, markdown_content="Page 1 content"),
            PageResult(page_number=2, markdown_content="Page 2 content")
        ])
        
        parser = PDFParser(engine="simple")
        # We can pass a dummy path because we mocked the process method
        # But PDFParser checks if file exists first.
        # So we need a real dummy file.
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
            doc = parser.parse(tmp.name)
            
            assert "<!-- page_number: 1 -->" in doc.content
            assert "Page 1 content" in doc.content
            assert "<!-- page_number: 2 -->" in doc.content
            assert "Page 2 content" in doc.content
            assert doc.metadata['engine'] == 'simple'

def test_pdf_parser_engine_selection():
    parser = PDFParser(engine="mineru")
    assert parser.engine_name == "mineru"
    # assert isinstance(parser.engine, MinerUEngine) # Need to import MinerUEngine to check
