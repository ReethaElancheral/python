# 26. PDF Text Extractor 
# Objective: Extract text from PDFs. 
# Requirements: 
#  Modules: Use PyPDF2. 
#  File Handling: Read PDFs. 
#  String Operations: Clean extracted text. 
#  Exception Handling: Encrypted PDFs. 
#  Functions: extract_text(pdf_path). 
#  Generator: Yield page-by-page text. 


from extractor.core import extract_text

def main():
    print("📄 PDF Text Extractor")
    pdf_path = input("Enter path to PDF file: ").strip()

    try:
        print("\nExtracted text by page:\n")
        for i, page_text in enumerate(extract_text(pdf_path), start=1):
            print(f"--- Page {i} ---")
            print(page_text)
            print()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
