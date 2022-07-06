# Author Name: Harsh Vyapari
# Author Email: ardostree2001@outlook.com
# Date of Creation: 09/06/2022


# Description : So basically, I designed this script as one day challenge
# for transferring files for the location given according to the users which automate 
# the task for file transfer in windows.


import os, shutil as files, time as t

# Four global variables which are going to perform this task
global src_folder
global des_folder
global file_dir


print("WARNING: Some dialogues in this app are pun intended, so please don't take it seriously (Not that I care!!)")
t.sleep(5)

# The below function is CLI menu driven function.
# This function helps in selecting the options.
# START
def main_menu():

        print("\n\n******MAIN MENU******: \n 1.Copy Files(According to format)")
        print("\n 3.Copy Files\n 4.Move Files")
        print("\n 5.Change the path \n\n \"Enter '0' to Exit\"")


        try:
                option = int(input("\n Your Option: "))

        except ValueError:
                print("You entered a character/decimal instead of digit, Are you serious!!, \"Please only select number I beg of you.\"")
                t.sleep(5)
                return main_menu()

        # First Option Selection
        if option == 1:
                print("\nFirst Option is Selected:")
                format_copy()
                t.sleep(2)
                return main_menu()

        # Second option Selector
        elif option == 2:
                print("\nSecond Option is Selected:")
                format_move() 
                t.sleep(2)
                return main_menu()
        
        elif option == 3:
                print("\nThird option is Selected:")
                direct_copy()
                t.sleep(2)
                return main_menu()

        elif option == 4:
                print("\nFourth option is Selected:")
                direct_move()
                t.sleep(2)
                return main_menu()

        elif option == 5:
                print("\nFifth option is selected")
                t.sleep(2)
                return main_menu()

        elif option == 0:
                print("\nKono CLI apuri o go riyō itadaki arigatōgozaimasu (English Translation: Thank you for using this CLI app)!!!")
                t.sleep(3)
                exit()
        
        else:
                print("Option Selection Error!!, Please select option seriously or I'll beat you to death")
                return main_menu()
# END

# All Function Related to Menu Option 
# (START)
def format_copy():
        print("\nFormat copy function")
        return main_menu()

def format_move():
        print("\nFormat move function")
        return main_menu()

def direct_copy():
        print("\nDirect copy function")
        return main_menu()

def direct_move():
        print("\nDirect move function")
        return main_menu()
# (END)

# All File name, path are stored here.
def user_data_collector():
        print("\n****** Select the Data **************")
        des_folder = input("Destination: ")
        des_folder = input("Source: ")
        file_dir = input("File Directive: ")
        t.sleep(2)
        main_menu()

user_data_collector()