import PyPDF2

with open('.\dummy.pdf', 'br') as file:
    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)      #gives us the number of pages
    #print(reader.getPage(0))    #gives us the page object - looks a little crazy

    page = reader.getPage(0)
    #print(page.rotateCounterClockwise(90))     #this wont wonrk as we are just storing it somewhere in memory - we need to create this somewehre
    
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilted_dummy.pdf', 'wb') as  tilted_file:
        writer.write(tilted_file)
