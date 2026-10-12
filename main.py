from pathlib import Path

def readfileandfloder() :
    path = Path('')
    items = list(path.rglob('*'))
    print("\n == Files and Folders ==")

    for i, item in enumerate(items):
        print(f"{i+1} : {item} ")


def createfile():
    try:
        readfileandfloder()
        name = input("Enter your file name: ")
        p = Path(name)

        if not p.exists() :
            with open(p,"w") as fs :
                data = input("What you want to write in this file :- ")
                fs.write(data)

            print("\nFILE CREATED SUCCESSFULLY")

        else:
            print("This file already exist")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile() :
    try :
        readfileandfloder()
        name = input("Which file you want to read :- ")
        p = Path(name)

        if p.exists() and p.is_file() :
            with open(p,'r') as fs :
                data = fs.read()
                print(data)

            print("\nFILE READ SUCCESSFULLY")

        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile() :
    try :
        readfileandfloder()
        name = input("Which file you want to update :- ")
        p = Path(name)

        if p.exists() and p.is_file() :
            print("\n1. Rename the file")
            print("2. Overwrite the file contents")
            print("3. Append content to the file")

            res = int(input("Select your option: "))

            if res == 1 :
                name2 = input("Enter your new file name: ")
                p2 = Path(name2)

                if p2.exists():
                    print("File name already exists.")
                else:
                    p.rename(p2)
                    print("\nFILE RENAMED SUCCESSFULLY")

            elif res == 2 :
                with open(p,'w') as fs :
                    data = input("Enter the new content: ")
                    fs.write(data)
                    print("\nFILE CONTENTS OVERWRITTEN SUCCESSFULLY")

            elif res == 3 :
                with open(p,'a') as fs :
                    data = input("Enter the content to append: ")
                    fs.write(" "+data)
                    print("\nCONTENT APPENED SUCCESSFULLY")

            else :
                print("Invalid option. ")
                return

        else:
            print("The file does not exist")

    except Exception as err :
        print(f"An error occured as {err}")


def deletefile() :
    try :
        readfileandfloder()
        name = input("which file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("FILE REMOVED SUCCESSFULLY")

        else:
            print("No such file exist")


    except Exception as err :
            print(f"An error occured as {err}")


while True :
    print("\n==== FILE MANAGEMENT SYSTEM ====")
    print("1. Create file")
    print("2. Read file")
    print("3. Update file")
    print("4. Delete file")
    print("5. List files and folders")
    print("6. Exit")

    choice = int(input("Please tell your response: "))

    if choice == 1 :
        createfile()

    elif choice == 2 :
        readfile()

    elif choice == 3 :
        updatefile()

    elif choice == 4 :
        deletefile()

    elif choice == 5 :
        readfileandfloder()

    elif choice == 6 :
        print("Thank you for using the File Management System.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")