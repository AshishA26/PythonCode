import PyPDF2

def load_pdf(filename):
    f = open(filename, 'rb')
    return PyPDF2.PdfFileReader(f)

def add_to_writer(pdf, writer, start, end):
    for i in range(start-1, end):
        writer.addPage(pdf.getPage(i))

print('Welcome to the PDF Merger!')

filename1 = input("Please type the filename of the first file: ")
filename2 = input("Please type the filename of the second file: ")
filename3 = input("Please type the filename of the third file: ")

pdf1 = load_pdf(filename1)
pdf2 = load_pdf(filename2)
pdf3 = load_pdf(filename3)

pdf1_pages = pdf1.getNumPages()
pdf2_pages = pdf2.getNumPages()
pdf3_pages = pdf3.getNumPages()

print ("{} has {} pages.".format(filename1, pdf1_pages))
start1 = int(input("Start on page: "))
end1 = int(input("End on page: "))

print ("{} has {} pages.".format(filename2, pdf2_pages))
start2 = int(input("Start on page: "))
end2 = int(input("End on page: "))

print ("{} has {} pages.".format(filename3, pdf3_pages))
start3 = int(input("Start on page: "))
end3 = int(input("End on page: "))

output_filename = input("Save new file as: ")

output_file = open(output_filename, 'wb')
writer = PyPDF2.PdfFileWriter()

add_to_writer(pdf1, writer, start1, end1)
add_to_writer(pdf2, writer, start2, end2)
add_to_writer(pdf3, writer, start3, end3)

writer.write(output_file)
output_file.close()
