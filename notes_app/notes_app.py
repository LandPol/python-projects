def loadFile(file_name):
    try:
        with open(file_name, 'r') as f:
            notes = []
            for line in f:
                line = line.strip()
                if line:
                    notes.append(line.split(','))
            return notes
    except FileNotFoundError:
        print("ERROR: File not found.")
        return []


def saveFile(notes, file_name):
    try:
        with open(file_name, 'w') as f:
            for note in notes:
                f.write(f"{note[0]},{note[1]}\n")
    except FileNotFoundError:
        print("ERROR: File not found.")

def createNote(notes, file_name):
    title = input("Input title of your note: ")
    desc = input("Now your description: ")
    notes.append([title, desc])
    saveFile(notes, file_name)
    print("Note created.")

def editNote(notes, file_name, n):
    if 1 <= n <= len(notes):
        note = notes[n - 1]
        new_title = input("New title (leave empty to keep current): ")
        new_desc = input("New description (leave empty to keep current): ")

        if new_title.strip():
            note[0] = new_title
        if new_desc.strip():
            note[1] = new_desc
        
        saveFile(notes, file_name)
        print("Note edited correctly.")
    else:
        print("ERROR: Note with this number does not exist.")

def deleteNote(notes, file_name, n):
    if 1 <= n <= len(notes):
        removed = notes.pop(n - 1)
        saveFile(notes, file_name)
        print(f"Note {removed[0]} removed correctly.")
    else:
        print("ERROR: Note with this number does not exist.")

def printNotes(notes):
    print("\n")
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note[0]} - {note[1]}")
    print("\n")     
        
def menu():
    while True:
        file_name = 'notes.txt'
        print("--- NOTES APP ---")
        print("1. Print notes")
        print("2. Create notes")
        print("3. Edit notes")
        print("4. Delete notes")
        print("5. End")
        while True:
            try:
                m = int(input("Choose your action: "))
                break
            except ValueError:
                print("ERROR: Invalid value.")
        
        notes = loadFile(file_name)

        if m == 1:
            printNotes(notes)
        elif m == 2:
            createNote(notes, file_name)
        elif m == 3:
            printNotes(notes)
            while True:
                try:
                    n = int(input("Choose note ID to edit: "))
                    break
                except ValueError:
                    print("ERROR: Invalid value.")
            editNote(notes, file_name, n)

        elif m == 4:
            printNotes(notes)
            while True:
                try:
                    n = int(input("Choose note ID to remove: "))
                    break
                except ValueError:
                    print("ERROR: Invalid value.")
            deleteNote(notes, file_name, n)
        elif m == 5:
            print("Goodbye")
            break

menu()