"""
PDF utilities: load, strip OCR layer, save PDF, image extraction.
"""

import fitz  # PyMuPDF

def load_pdf(pdf_path):
    """Load a PDF and return PyMuPDF document object."""
    return fitz.open(pdf_path)

def strip_ocr_layer(pdf_path):
    """
    Remove text/OCR layer from PDF, return list of images (one per page).
    Returns: [PIL.Image or ndarray]
    """
    doc = fitz.open(pdf_path)
    images = []
    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img_bytes = pix.tobytes("png")
        from PIL import Image
        from io import BytesIO
        images.append(Image.open(BytesIO(img_bytes)))
    return images

def save_pdf(images, output_path):
    """
    Save a list of images as a PDF (without OCR/text layer).
    """
    from PIL import Image
    pil_images = [img.convert("RGB") for img in images]
    pil_images[0].save(output_path, save_all=True, append_images=pil_images[1:])

