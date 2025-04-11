import PyPDF4

f = open('Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF4.PdfFileReader(f)
print(pdf_reader.numPages)
page_1 = pdf_reader.getPage(0)
page_one_text = page_1.extractText()
print(page_one_text)

f.close()


with open('Working_Business_Proposal.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)
    first_page = pdf_reader.getPage(0)


    pdf_writer = PyPDF4.PdfFileWriter()
    print(type(first_page))
    pdf_writer.addPage(first_page)

    pdf_output = open('Some_Brand_New_Doc.pdf','wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()


with open('Working_Business_Proposal.pdf', 'rb') as pdf_file:
    pdf_text = []

    pdf_reader = PyPDF4.PdfFileReader(pdf_file)

    for num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(num)
        pdf_text.append(page.extractText())