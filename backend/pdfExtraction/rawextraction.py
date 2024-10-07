import pypdf
import os

def extract_raw_text(pdf_path):
    try:
        pdf_path = os.path.normpath(pdf_path)
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file {pdf_path} does not exist.")
        
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            raw_text = []
            
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                if text.strip():  # Only add non-empty pages
                    raw_text.append(f"--- Page {page_num} ---\n{text}\n")
            
        return '\n'.join(raw_text)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return ""
    except pypdf.errors.PdfReadError as e:
        print(f"Error reading PDF: {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

# Usage
base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(base_dir, '../../testasset/test.pdf')
output_file_path = os.path.join(base_dir, 'extracted_text.txt')
try:
    raw_text = extract_raw_text(pdf_path)
    if raw_text:
        ##print(raw_text)
        print("...")
        print(f"Total characters extracted: {len(raw_text)}")
        
        # Write the extracted text to a file.txt
        # for unix as horrible to read in bash

        # with open(output_file_path, 'w', encoding='utf-8') as output_file:
        #     output_file.write(raw_text)
        
        # print(f"Text successfully written to {output_file_path}")
    else:
        print("No text was extracted from the PDF.")
except Exception as e:
    print(f"An error occurred: {e}")