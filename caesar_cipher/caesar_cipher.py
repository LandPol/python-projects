def loadFile(fileName):
    with open(fileName, 'r') as f:
        return f.read()

def saveFile(fileName, uploadedFile):
    with open(fileName, 'w') as f:
        f.write(uploadedFile)

def encrypting(text, k):
    key = k
    newText = ""
    for char in text:
        if char.isupper():
            newText += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            newText += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            newText += char
        key += 1
    return newText


def decrypting(text, k):
    key = k
    newText = ""
    for char in text:
        if char.isupper():
            newText += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            newText += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            newText += char
        key += 1
    return newText

def menu():
    while True:
        print("\n --- Caesar Cipher --- \n")
        print("1. Encrypting")
        print("2. Decrypting")
        print("3. End")
        while True:
            try:
                m1 = int(input("Choose your action: "))
                break
            except ValueError:
                print("ERROR: Invalid acition")
        if m1 == 3:
            break
        if  m1 == 1 or m1 == 2:
            while True:
                print("\n Choose type of data:")
                print("1. file.txt")
                print("2. Text in terminal")
                print("3. End")
                try:
                    m2 = int(input("Choose your action: "))
                    break
                except ValueError:
                    print("ERROR: Invalid acition")
            if m2 == 3:
                break
            if m2 == 1 or m2 == 2:
                if m2 == 1:
                    fileName = input("Input name of your file: ")
                if m2 == 2:
                    text = input("Input your text: ")
                while True:
                    try:
                        key = int(input("Input your key: "))
                        break
                    except ValueError:
                        print("ERROR: Invalid key")
                print('\n')
                if m1 == 1 and m2 == 1:
                    file = loadFile(fileName)
                    newFile = encrypting(file, key)
                    saveFile(fileName, newFile)
                    print(newFile)

                elif m1 == 2 and m2 == 1:
                    file = loadFile(fileName)
                    newFile = decrypting(file, key)
                    saveFile(fileName, newFile)
                    print(newFile)

                elif m1 == 1 and m2 == 2:
                    newText = encrypting(text, key)
                    print(newText)
                
                elif m1 == 2 and m2 == 2:
                    newText = decrypting(text, key)
                    print(newText)
            
        
menu()            
