import sys
import re
import PyPDF2

#taking inputs - ignoring the first argument, which is the name of the script itself.

inputs = sys.argv[1:]

#check if files are a pdf with regex
def pdf_watermark(list_files, watermarkpage):
    pdfPattern = re.compile(r'^(.*)\.pdf$')

    for file in list_files:
        #checking if the file is a pdf 
        filecheck = pdfPattern.search(file)
        if filecheck != None:
            #getting the file name withouth the .pdf at the end
            filename = filecheck.group()
            fileprefix = filecheck.group(1)

            with open(filename, 'rb') as read_file:             #Open the PDF file for reading ('rb' mode)
                read_pdf = PyPDF2.PdfFileReader(read_file)      #Create a PdfFileReader object
                watermarked_pdf = PyPDF2.PdfFileWriter()        #Create a new PdfFileWriter object for the watermarked PDF file.

                #watermarking each page
                for page in range(read_pdf.getNumPages()):      #This will iterate over each page in the PDF file.
                    print(f"Processing page {page+1} of {read_pdf.getNumPages()}")
                    pdf_page = read_pdf.getPage(page)       #this gets each page
                    pdf_page.mergePage(watermarkpage)       #this merges the page with watermark file
                    watermarked_pdf.addPage(pdf_page)       #ths adds the resulting watermarked page to the watermarked_pdf object.
                
                #write new watermarked_file and append the name with '_watermarked' page
                write_filename = fileprefix + '_watermark.pdf'
                with open(write_filename, 'wb') as write_file:
                    watermarked_pdf.write(write_file)
                print(f'{write_filename} has succesfully been created for you good sir')

        #will let you know if one of the files is not a pdf
        else:
            print(f'Ignoring file {file}, as it is not a PDF document.')

def watermark_page(pdffile):
    #checking if the watermark file is inface a pdf
    pdfPattern = re.compile(r'^(.*)\.pdf$')
    watermarkfilecheck = pdfPattern.search(pdffile)
    
    #if the file is a pdf, open & read the file then return the page as an object
    if watermarkfilecheck != None:
        read_pdf = PyPDF2.PdfFileReader(open(pdffile, 'rb'))
        watermark_page = read_pdf.getPage(0)
        return watermark_page
    #if the file is not a pdf
    else:
        print('Watermark is not a PDF file!')
        return None

wtr_page = watermark_page(inputs[-1])  #This will get the last argument as the watermark file to be merged.
 
#finally call the function
pdf_watermark(inputs[:-1], wtr_page)