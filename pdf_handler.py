from PyPDF2 import PdfWriter, PdfReader
import os

def merge():
    merger = PdfWriter()

    files = input("Enter pdfs' paths: \n").split(" ")
    merged_file_name = input("Enter new file name: \n")

    for p in files:
        merger.append(p)
    
    merger.write(merged_file_name)
    merger.close()


def split():
    path_name = input("Enter pdf file path\n")
    file_name = os.path.splitext(path_name)[0]

    reader = PdfReader(path_name)

    os.makedirs(file_name, exist_ok=True)
    output_path = os.path.join(os.getcwd(), file_name)

    for index, p in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(p)

        with open(f'{output_path}/{file_name}_{index}.pdf', 'wb') as f:
            writer.write(f)






