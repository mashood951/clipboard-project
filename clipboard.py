import keyboard
import pyperclip as pc
import sys
import os
from time import sleep


def main():
    print("************    Mas ;)    ************\n\n")

    count = 0

    choice = input("Do you want to open the file? (Y/n) ")

    if choice == 'y' or choice == 'Y':
        if os.path.exists('output') == True:
            os.chdir('output')
            if os.path.exists('clipboard_history.txt') == False:
                print('You deleted the file silly. Now enter "n" next time.')
                sleep(2)
                os.system('cls')
                main()

            elif os.path.exists('clipboard_history.txt'):
                os.system('clipboard_history.txt')
        else:
            print('Enter "n" first dummy.')
            sleep(2)
            os.system('cls')
            main()

    elif choice == 'n' or choice == 'N':
        copying_limit = int(input("Enter copying limit: "))

        if copying_limit == 0:
            print("You entered 0 and you cannot save anything in clipboard history.")
            sys.exit()

        if os.path.exists('output') == False:
            os.system('mkdir output')

        os.chdir('output')

        file = open("clipboard_history.txt", "+a")

        if os.stat("clipboard_history.txt").st_size == 0:
            file.write(
                "/*******************CLIPBOARD HISTORY*******************\\\n\n")

        while True:
            if keyboard.is_pressed('ctrl + c'):
                copied_text = pc.waitForNewPaste()
                file.write("{0}".format(copied_text) + "\n\n")
                count += 1
                if count == copying_limit:
                    break
            if keyboard.is_pressed('alt + b'):
                print('You pressed right.')
                break

        file.close()

    elif choice != 'y' or choice != 'Y' or choice != 'n' or choice != 'N':
        print("Wrong input. Try again...")
        sleep(1)
        os.system('cls')
        main()


if __name__ == "__main__":
    main()
