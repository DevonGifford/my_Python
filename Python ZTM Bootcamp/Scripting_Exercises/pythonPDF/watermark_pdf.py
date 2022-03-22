import sys
import PyPDF2
 
watermark_doc = sys.argv[1]
target_doc = sys.argv[2]
 
watermark = PyPDF2.PdfFileReader(watermark_doc)
doc_reader = PyPDF2.PdfFileReader(target_doc)
writer = PyPDF2.PdfFileWriter()

for doc_page in doc_reader.pages:
    doc_page.mergePage(watermark.getPage(0))
    writer.addPage(doc_page)
 
with open('doc_watermarked.pdf', 'wb') as file:
    writer.write(file)