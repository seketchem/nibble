# nibble

## OCR PDF Processor & Inspector

**nibble** is a Python tool for reprocessing and correcting OCR layers in PDFs.
- Removes inaccurate OCR from PDFs.
- Re-processes using Tesseract.
- Allows users to inspect and hand-edit OCR via a visual interface.
- Exports clean, corrected, searchable PDFs.

### Quickstart

1. Install requirements:
	pip install -r requirements.txt
	
2. To process a PDF:
	python main.py input_pdfs/mydoc.pdf --output output_pdfs/mydoc_ocr.pdf
	
3. To launch inspector:
	python main.py --inspect
	
### Modules

- `main.py` – CLI and workflow orchestrator
- `pdf_utils.py` – PDF I/O and image conversion
- `ocr_utils.py` – Tesseract OCR logic
- `inspector.py` – Streamlit OCR inspector interface

---

**Work in progress!**  
The prototype currently supports image extraction, basic OCR, and an inspector UI.
OCR-to-PDF embedding is a stub for now—advanced text layer support coming soon.