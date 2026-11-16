
def savefile(file,words):

    filehandler=open(file,"w")

    for i in range(len(words)):

        filehandler.write(words[i]+"\n")

    filehandler.close()


def turnword(word):

    newword=""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in word:

        if i in alphabet:

            index=alphabet.index(i)

            if index < 13:
                newindex=index+13
            else:
                newindex=index-13

            newword+=alphabet[newindex]

        elif i in alphabet2:

            index=alphabet2.index(i)

            if index < 13:
                newindex=index+13
            else:
                newindex=index-13

            newword+=alphabet2[newindex]

        else:
            newword+=i

    return newword


def main():

    newwordlist=[]

    print("Program starting.\n")

    print("Collecting plain text rows for ciphering.")

    word=input("Insert row(empty stops): ")

    while word != "":

        content=turnword(word)

        newwordlist.append(content)

        word=input("Insert row(empty stops): ")

    print("\nChoose operation:")
    print("1. Show ciphered text")
    print("2. Save ciphered text")

    choice=input("Select operation: ")

    if choice == "1":

        print("\n#### Ciphered text ####")

        for i in range(len(newwordlist)):
            print(newwordlist[i])

    elif choice == "2":

        print("\n#### Ciphered text ####")

        file=input("Insert filename to save: ")

        if file == "":
            print("File name not defined.\nAborting save operation.")
        else:
            savefile(file,newwordlist)
            print("Ciphered text saved!")

    else:
        print("Invalid choice.")

    print("Program ending.")


if __name__=="__main__":
    main()
