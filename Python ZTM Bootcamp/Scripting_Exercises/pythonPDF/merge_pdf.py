import PyPDF2
import sys

inputs = sys.argv[1:]  #this will grab all the arguments (except 0 - which will be our script file) and put them into a list

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print (pdf)
        merger.append(pdf)
    merger.write('your_new_merged_file.pdf')
    print("The PDF's have been merger, Sir!")

pdf_merger(inputs)
