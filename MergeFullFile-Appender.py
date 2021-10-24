from PyPDF2 import PdfFileMerger

pdfs = ['01_AbhinavAgrahari_CoverLetter.pdf', '02_AbhinavAgrahari_Resume.pdf', '03_AbhinavAgrahari_Transcript.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
