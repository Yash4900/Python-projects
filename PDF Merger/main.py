from PyPDF2 import PdfFileMerger
import os

filename = input('Enter file name: ')

files = os.listdir('./files')

merger = PdfFileMerger()

for file in files:
    merger.append(f"./files/{file}")

merger.write(f"./{filename}.pdf")
merger.close()