import re
import os
import fitz

def extract_equations(pdf_path):
    doc = fitz.open(pdf_path)
    equations = []

    for page in doc:
        # Extract text from the page
        text = page.get_text()
        
        # Simple heuristic: look for text enclosed in $ signs
        # This assumes equations are demarcated by $ in the PDF
        eq_start = text.find('$')
        while eq_start != -1:
            eq_end = text.find('$', eq_start + 1)
            if eq_end != -1:
                equation = text[eq_start+1:eq_end]
                equations.append(equation)
                eq_start = text.find('$', eq_end + 1)
            else:
                break

    return equations

# Usage
base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(base_dir, '../../testasset/test.pdf')

extracted_equations = extract_equations(pdf_path)

print(f"Total equations found: {len(extracted_equations)}")

for i, eq in enumerate(extracted_equations, 1):
    print(f"Equation {i}: {eq}")
