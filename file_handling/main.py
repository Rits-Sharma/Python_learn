# r - read mode, w - created files or overrides, a - appends to end of file, x - created a new file, fails if it is already exists



import os
from pathlib import Path

def pathDisplay():
    print("Files:", end="")
    p = Path('')
    items = list(p.rglob('*'))
    for i, item in enumerate(items):
        if i != 0:
            print(f"      {i+1}. {item}")
        else:
            print(f"{i+1}. {item}")

def createFile():
    pathDisplay()
    name = input("Enter name of file:- ")
    p = Path(name)
    try:
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter data to the file: ")
                fs.write(data)
            fs.close()
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as e:
        print(f"There is an error: {e}")

def readFile():
    pathDisplay()
    name = input("Enter file name: ")
    p = Path(name)
    try:
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                print(fs.read())
            fs.close()
            print("File read successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"There is an error: {e}")

def updateFile():
    try:
        pathDisplay()
        name = input("Enter file to update:")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1. for changing the name of your file")
            print("2. for overwriting the content of your file")
            print("3. for appending the content of your file")

        response = int(input("Enter your choice: "))
        if response == 1:
            name2 = input("Tell your file name: ")
            p2 = Path(name2)
            p.rename(p2)

        if choice == 2:
            with open(p, 'w') as fs:
                data = input("Enter data to the file: ")
                fs.write(data)
            fs.close()
            print("File updated successfully")

        if response == 3:
            with open(p, 'a') as fs:
                data = input("Enter data to the file to be append: ")
                fs.write(data)
            fs.close()
            print("File updated successfully")
    except Exception as e:
        print(e)

def deleteFile():
    try:
        pathDisplay()
        name = input("Enter file to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("File deleted successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(e)

choice = 1
while choice != 0:
    print("Menu:")
    print("1. Create a new file:")
    print("2. Read a file:")
    print("3. Update a file:")
    print("4. Delete a file:")
    print("5. Display all file:")
    print("0. Exit:")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        createFile()
    elif choice == 2:
        readFile()
    elif choice == 3:
        updateFile()
    elif choice == 4:
        deleteFile()
    elif choice == 5:
        pathDisplay()
    elif choice == 0:
        print("Exiting...")
    else:
        print("Invalid choice")

