from glob import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

root = input('Input root folder for input PDFs : ')
root_output = input('Input root folder for output PDFs : ')
pdf_list = []

for i in glob(root + '\*'):
    if i.split('.')[-1] == 'pdf':
        pdf_list.append(i)

pdf_list.sort()

for i in pdf_list:
    print(i)

for i in range(0, len(pdf_list), 2):
    merger = PdfFileMerger()
    merger.append(PdfFileReader(open(pdf_list[i], 'rb')))
    merger.append(PdfFileReader(open(pdf_list[i+1], 'rb')))
    merger.write(root_output + pdf_list[i].split('\\')[-1])
