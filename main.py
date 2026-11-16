
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(character, alphabet):

    if character in alphabet:

        index=alphabet.index(character)

        if index < 13:
            newindex=index+13
        else:
            newindex=index-13

        return alphabet[newindex]

    else:
        return character


def rot13(text):

    newtext=""

    for i in text:

        if i in LOWER_ALPHABETS:
            newtext+=shiftCharacter(i,LOWER_ALPHABETS)

        elif i in UPPER_ALPHABETS:
            newtext+=shiftCharacter(i,UPPER_ALPHABETS)

        else:
            newtext+=i

    return newtext


def writeFile(filename,content):

    filehandler=open(filename,"w")

    filehandler.write(content)

    filehandler.close()


def main():

    newword=""

    print("Program starting.\n")

    print("Collecting plain text rows for ciphering.")

    word=input("Insert row(empty stops): ")

    while word != "":

        content=rot13(word)

        newword+=content+"\n"

        word=input("Insert row(empty stops): ")

    print("\nChoose operation:")
    print("1. Show ciphered text")
    print("2. Save ciphered text")

    choice=input("Select operation: ")

    if choice == "1":

        print("\n#### Ciphered text ####")
        print(newword)

    elif choice == "2":

        print("\n#### Ciphered text ####")

        filename=input("Insert filename to save: ")

        if filename == "":
            print("File name not defined.\nAborting save operation.")

        else:
            writeFile(filename,newword)
            print("Ciphered text saved!")

    else:
        print("Invalid choice.")

    print("Program ending.")


if __name__=="__main__":
    main()
