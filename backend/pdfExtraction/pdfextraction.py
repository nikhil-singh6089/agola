import pypdf
import re
import os

def is_likely_equation(line):
    # Check for common equation indicators
    equation_indicators = [
        r'\b[a-zA-Z]\s*=',  # Variable assignments
        r'\b\w+\([^)]*\)',  # Function-like expressions
        r'[+\-*/^]',        # Mathematical operators
        r'\bsum\b',         # Common mathematical terms
        r'\bint\b',
        r'\blim\b',
        r'\bmax\b',
        r'\bmin\b',
        r'[{(\[]',          # Brackets often used in equations
        r'[≤≥±∫∑∏√]'        # Mathematical symbols
    ]
    return any(re.search(pattern, line) for pattern in equation_indicators)

def is_roman_numeral(s):
    pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, s, re.IGNORECASE))

def is_header(line):
    # Check for Roman numeral headers
    if re.match(r'^[IVXLCDM]+\.\s', line, re.IGNORECASE):
        return True
    
    # Check for numeric headers (e.g., "1.", "1.1.", "1.1.1.")
    if re.match(r'^\d+(\.\d+)*\.\s', line):
        return True
    
    # Check for alphabetic subsections (e.g., "A.", "a)", "(a)")
    if re.match(r'^[A-Za-z]\.|\([A-Za-z]\)|\s[A-Za-z]\)\s', line):
        return True
    
    # Check for numeric subsections (e.g., "1.", "(1)")
    if re.match(r'^\d+\.|\(\d+\)', line):
        return True
    
    # Check for all uppercase lines (potential headers)
    if line.isupper() and len(line) > 3:  # Assuming headers are at least 4 characters long
        return True
    
    return False

def extract_text_with_headers(pdf_path):
    try:
        pdf_path = os.path.normpath(pdf_path)
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file {pdf_path} does not exist.")
        
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        
        lines = text.split('\n')
        current_header = []
        current_content = []
        result = []
        
        for line in lines:
            line = line.strip()
            if not line or is_likely_equation(line) :
                continue
            
            if is_header(line):
                if current_header and current_content:
                    result.append({
                        'header': ' '.join(current_header),
                        'content': ' '.join(current_content)
                    })
                current_header = [line]
                current_content = []
            else:
                if current_header:
                    current_content.append(line)
                else:
                    current_header = [line]
        
        if current_header and current_content:
            result.append({
                'header': ' '.join(current_header),
                'content': ' '.join(current_content)
            })
        
        return result
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except pypdf.errors.PdfReadError as e:
        print(f"Error reading PDF: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Usage
base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(base_dir, '../../testasset/test.pdf')

try:
    extracted_data = extract_text_with_headers(pdf_path)

    if extracted_data:
        # Print the extracted data
        for item in extracted_data:
            print(f"Header: {item['header']}")
            print(f"Content: {item['content']}")  # Print first 100 characters of content
            print()
    else:
        print("No data was extracted from the PDF.")
except Exception as e:
    print(f"An error occurred: {e}")