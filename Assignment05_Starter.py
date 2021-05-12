# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SSparks,2021.05.09,Added code to begin assignment 5
# SSparks,2021.05.10,Continued working on assignment 5
# SSparks,2021,05.11,Finalized assignment 5 for submission
# ------------------------------------------------------------------------ #
import os.path
from os import path
# -- Data -- #
# declare variables and constants
objFile = None # An object that represents a file
strFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
lstRow = []

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"Task":lstRow[0],"Priority":lstRow[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        dicRow = {"Task":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoveTask = input("Which task would you like to remove? ")
        blnRemovedTask = False
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(strRemoveTask == str(list(dict(lstTable[intRowNumber]).values())[0])):
                del lstTable[intRowNumber]
                blnRemovedTask = True
            intRowNumber += 1
        if(blnRemovedTask == True):
            print(strRemoveTask + " was removed.")
        else:
            print(strRemoveTask + " is not on the list.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"].strip() + "\n")
        objFile.close()
        input("Data saved to file! 'Enter' for main menu. ")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("I hope you remembered to save! Goodbye.")
        break  # and Exit the program
