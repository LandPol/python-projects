from PyPDF2 import PdfReader, PdfWriter

def printPdf(file_name):
    try:
        with open(file_name, 'rb') as f:
            reader = PdfReader(f)

            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    print(text)
                else:
                    print(f"[Page {i + 1}] No extractable text.")
                
    except FileNotFoundError:
        print("ERROR: File not found.")

def savePdf(writer, file_new_name):
    with open(file_new_name, 'wb') as f:
        writer.write(f)
        print("File saved correctly.")
    
def mergePdf(pdfs_list):
    pdf_writer = PdfWriter()

    for pdf in pdfs_list:
        reader = PdfReader(pdf)
        for page in reader.pages:
            pdf_writer.add_page(page)
    
    name = input("Input name of your merged file: ")
    savePdf(pdf_writer, name)
    return name

def splitPdf(file_name, pages):
    try:
        with open(file_name, 'rb') as f:
            reader = PdfReader(f)
            
            for i, page in enumerate(reader.pages):
                if i in pages:
                    writer = PdfWriter()
                    writer.add_page(page)
                    name = file_name.replace(".pdf", "")
                    savePdf(writer, f'{name}_{i + 1}.pdf')
                    print(f'Created {name}_{i + 1}.pdf')
    except FileNotFoundError:
        print("ERROR: File not found.")

def encryptPdf(file_name, pswd):
    writer = PdfWriter()
    try:
        with open(file_name, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                writer.add_page(page)
        writer.encrypt(pswd)
        name = file_name.replace(".pdf", "")
        savePdf(writer, f'{name}_encrypted.pdf')
        print(f"Created {name}_encrypted.pdf")
    except FileNotFoundError:
        print("ERROR: File not found.")

def decryptPdf(file_name, pswd):
    writer = PdfWriter()
    try:
        with open(file_name, 'rb') as f:
            reader = PdfReader(f)
            if reader.is_encrypted:
                reader.decrypt(pswd)
                for i in range(reader.numPages):
                    writer.add_page(reader.pages[i])
                name = file_name.replace(".pdf", "")
                savePdf(writer, f'{name}_decrypted.pdf')
                print("File descrypted successfully.")
            else:
                print("File already descrypted.")
    except FileNotFoundError:
        print("ERROR: File not found")



def menu():
    while True:
        print("\n")
        print("--- PDF MERGER AND SPLITER ---")
        print("1. Merge")
        print("2. Split")
        print("3. Encrypt PDF")
        print("4. Descrypt PDF")
        print("5. Print PDF")
        print("6. End")
        print("\n")
        while True:
            try:
                m = int(input("Choose your action: "))
                break
            except ValueError:
                print("ERROR: Invalid action.")
        if m == 1:
            files_list = ['sample1.pdf', 'sample2.pdf', 'sample3.pdf']
            files_to_merge = []
            n = 0
            while n < 3:
                x = input(f"Do you want to merge sample{n + 1}.pdf? T/n: ")
                if x == 't' or x == 'T':
                    files_to_merge.append(files_list[n])
                n += 1
            mergePdf(files_to_merge)
        elif m == 2:
            name = input("Input name of file to be splited: ")
            pages_input = input('Input pages to be splited (eg: 1-3,5): ')
            pages_input = pages_input.split(',')
            pages = []
            for n in pages_input:
                if '-' in n:
                    start, end = map(int, n.split('-'))
                    for i in range(start, end + 1):
                        pages.append(i)
                else:
                    pages.append(int(n))
            splitPdf(name, pages)
        elif m == 3:
            name = input("Input name of file to be encrypted: ")
            pswd = input("Input your password: ")
            encryptPdf(name, pswd)
        elif m == 4:
            name = input("Input name of file to be decrypted: ")
            pswd = input("Input your password: ")
            decryptPdf(name, pswd)
        elif m == 5:
            name = input("Input name of file to be printed: ")
            printPdf(name)
        elif m == 6:
            break

menu()