# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Marita Quiroz,05/17/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objFile:
  lstRow = row.split(",")
  # Strip \n from row, when being saved to dictionary
  dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
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
        # Display Task, Priority header to user
        print("Task, Priority")
        for row in lstTable:
            # Display current task and priority values to user
            strData = row.get("Task") + "," + row.get("Priority")
            print(strData)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Ask user for input
        task = input("Enter a task: ")
        priority = input("Enter a priority: ")
        print(task, ", ", priority)
        # Save user input in dictionary row
        dicRow = {"Task": task, "Priority": priority}
        # Save dictionary row into list table
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # Find current length of list
        length = len(lstTable)
        # Subtract 1 since list locations start at 0
        itemLOC = length - 1
        # Confirm to user item being removed
        print("Item being removed is: ", lstTable[itemLOC])
        # Remove item from last location in list table
        lstTable.pop(itemLOC)
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # Open file to write
        objFile = open("ToDoList.txt", "w")
        # Confirm data being saved to user
        print("Data being saved to file: " + '\n')
        # Write list table to file
        for row in lstTable:
            # Need to save only Dictionary items to string
            # Without Task and Priority index names
            # Separate task and priority values with a "," in file
            strData = row.get("Task") + "," + row.get("Priority")
            # Confirm data being saved to user
            print(strData)
            # Save data (task, priority) to file, each on a new line
            objFile.write(strData + '\n')
        # Close file
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting program")
        break  # and Exit the program
