import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):             #get the number of pages
  page = template.getPage(i)                        #gets each page in the file
  page.mergePage(watermark.getPage(0))              #this will merge the file
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
  