"""
Launches the OCR inspector UI (Streamlit).
Handles PDF/image loading, OCR display, and manual correction interface.
"""

def launch_inspector():
    import os
    import streamlit as st
    from pdf_utils import load_pdf
    from ocr_utils import ocr_pdf

    st.set_page_config(page_title="Nibble OCR Inspector", layout="wide")
    st.title("Nibble OCR Inspector")

    uploaded_file = st.file_uploader("Upload PDF for inspection", type=["pdf"])
    if uploaded_file:
        # Temporary file workaround for PyMuPDF
        temp_path = "static/uploaded.pdf"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        doc = load_pdf(temp_path)
        st.sidebar.markdown("### Page Selection")
        page_num = st.sidebar.slider("Page", 1, len(doc), 1)
        page = doc[page_num - 1]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")

        st.image(img_bytes, caption=f"Page {page_num}")

        # OCR preview
        from PIL import Image
        from io import BytesIO
        img = Image.open(BytesIO(img_bytes))
        ocr_result = ocr_pdf([img])[0]

        # Display OCR text (stub, not parsed)
        st.subheader("OCR (Raw HOCR/XML output):")
        st.text_area("Editable OCR Output", ocr_result['hocr'].decode('utf-8'), height=300)

        # TODO: Parse hOCR and overlay bounding boxes and provide per-line editing

    st.info("To edit OCR output, select a page and review/correct the recognized text above.")
