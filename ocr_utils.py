"""
OCR utilities: Run Tesseract, process output, handle OCR data structures.
"""

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_pdf(images, lang="eng"):
    """
    Run OCR (Tesseract) on list of PIL images.
    Returns: List of dicts: [{'text': ..., 'boxes': [...]}] per page.
    """
    results = []
    for img in images:
        # Get OCR text with bounding box info (hOCR)
        hocr = pytesseract.image_to_pdf_or_hocr(img, extension='hocr', lang=lang)
        # Or get text only: text = pytesseract.image_to_string(img, lang=lang)
        results.append({'hocr': hocr})
    return results

def save_ocr_to_pdf(images, ocr_results, output_path):
    """
    Save OCR layer back into PDF as invisible searchable text.
    For prototype: store as PDF with hOCR or similar (advanced: true invisible layer).
    """
    # TODO: Implement PDF OCR layer insertion, possibly with pdfalto, ocrmypdf, or PyMuPDF.
    # For stub: save images as PDF as placeholder.
    from pdf_utils import save_pdf
    save_pdf(images, output_path)
    print("Warning: OCR text not yet embedded (stub only).")
