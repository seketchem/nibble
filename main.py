"""
Main CLI entry point for nibble OCR processor.
Handles argument parsing and orchestrates the workflow.
"""

import argparse
from pdf_utils import strip_ocr_layer, save_pdf, load_pdf
from ocr_utils import ocr_pdf, save_ocr_to_pdf
from inspector import launch_inspector

def process_pdf(input_path, output_path):
    # Step 1: Load and strip OCR
    pdf_images = strip_ocr_layer(input_path)
    # Step 2: Run OCR on each page
    ocr_results = ocr_pdf(pdf_images)
    # Step 3: Save new OCR-embedded PDF
    save_ocr_to_pdf(pdf_images, ocr_results, output_path)
    print(f"Processed PDF saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Nibble: OCR PDF Processor & Inspector")
    parser.add_argument("input", nargs="?", help="Input PDF file or folder")
    parser.add_argument("--output", "-o", help="Output PDF or folder")
    parser.add_argument("--inspect", action="store_true", help="Launch inspector UI")
    args = parser.parse_args()

    if args.inspect:
        launch_inspector()
    elif args.input:
        # Assume single file for now
        output = args.output or "output_pdfs/processed.pdf"
        process_pdf(args.input, output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
