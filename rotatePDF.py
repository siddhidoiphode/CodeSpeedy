from PyPDF2 import PdfReader, PdfWriter
def rotate_pdf(input_pdf_path, output_pdf_path, rotation_angle):
    # Create a PdfReader object to read the input PDF
    reader = PdfReader(input_pdf_path)
    
    # Create a PdfWriter object to write the rotated PDF
    writer = PdfWriter()
    
    # Loop through each page in the PDF
    for page in reader.pages:
        # Rotate the page by the specified angle
        page.rotate(rotation_angle)  # Use rotate instead of rotate_clockwise
        # Add the rotated page to the writer object
        writer.add_page(page)
    
    # Write the rotated pages to the output PDF file
    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":
    input_pdf = r"C:\Users\Siddhi Doiphode\Downloads\AI.pdf"  # Path to the input PDF file
    output_pdf = r"C:\Users\Siddhi Doiphode\Downloads\AI_output.pdf"  # Path to save the rotated PDF file
    rotation_angle = 90  # Rotation angle (90, 180, or 270 degrees)
    rotate_pdf(input_pdf, output_pdf, rotation_angle)
    print(f"Rotated PDF saved as {output_pdf}")

    



