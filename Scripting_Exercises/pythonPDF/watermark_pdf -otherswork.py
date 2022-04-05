# Build a tool that will apply a watermark to every page
# of the super.pdf file created in the last exercise
# or to any PDF file taken in as an argument
 
 
import PyPDF2
import sys
import os
 
 
def usage():
    print("""Please use the utility as follows:
>>> python watermarker.py FileToWatermark.pdf
where FileToWatermark.pdf is a PDF that exists""")
    exit()
 
 
if len(sys.argv) != 2:
    print("Incorrect number of arguments.")
    usage()
 
input_file = sys.argv[1]
 
if not os.path.isfile(input_file):
    print("File not found.")
    usage()
if not input_file.lower().endswith(r".pdf"):
    print("File is not a PDF.")
    usage()
 
 
def apply_watermark(pdf):
    # Open the file that the watermark file will be applied to
    with open(pdf, "rb") as file_to_watermark:
        original_pdf = PyPDF2.PdfFileReader(file_to_watermark)
        # Open the file containing the watermark to be applied
        with open(r".\PDFs\wtr.pdf", "rb") as watermark_file:
            watermark = PyPDF2.PdfFileReader(watermark_file).getPage(0)
            output_file = PyPDF2.PdfFileWriter()
            # Loop over pages in original PDF, merge the watermark page
            for i in range(original_pdf.getNumPages()):
                page = original_pdf.getPage(i)
                page.mergePage(watermark)
                output_file.addPage(page)
                # Write the watermarked pages to new PDF
                with open(r".\PDFs\watermarked.pdf", "wb") as watermarked_pdf:
                    output_file.write(watermarked_pdf)
 
 
if __name__ == "__main__":
    apply_watermark(input_file)