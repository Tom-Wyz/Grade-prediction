from pdfminer.high_level import extract_text
from reportlab.lib.colors import Color

def get_colored_rows(pdf_path, target_color='#FF0000'):
    colored_rows = []

    # Extract text using pdfminer
    text = extract_text(pdf_path)

    # Iterate through text lines
    for line in text.split('\n'):
        # Create a Color object from the target color
        color = Color(*[int(target_color[i:i+2], 16)/255.0 for i in (1, 3, 5)])
        
        # Check if the line has the specified color
        if line.startswith('<color rgb="{}"/>'.format(color)):
            colored_rows.append(line)

    return colored_rows

# Example usage
pdf_path = 'verRpt.pdf'
color_hex = '#cce6ff'  # Replace with the color you are looking for in hexadecimal format
result = get_colored_rows(pdf_path, color_hex)

print(result)
 