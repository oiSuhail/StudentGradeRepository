# This work done by group 13:
# Suhail Alhawi, 202181470, 50%
# Fahad AlSulami, 202037780, 50%

def studentsList(valueType = ""):                  # This function gets the data from the file 
    with open("Database.txt", "r") as database:    # and append each section as a list into a dictionary with its own key. The fucntion have 1 parameter which choose a specific data
        next(database) # Skipping first line in the file which is for titles
        info = {
            "id": [],
            "name": [],
            "absences": [],
            "exam1": [],
            "exam2": [],
            "total": []
        }
        for line in database: # Sort the data under its title as a key:value
            line = line.split(" | ")
            for studentInfo in range(len(line)):
                if studentInfo == 0:
                    info['id'].append(''.join(line[studentInfo].strip(" ")))
                    if valueType == "id": break                               # If a specific data is chosen the loop will end here so the program will run faster

                elif studentInfo == 1:
                    info['name'].append(''.join(line[studentInfo].strip(" ")))
                    if valueType == "name": break

                elif studentInfo == 2:
                    info['absences'].append(''.join(line[studentInfo].strip(" ")))
                    if valueType == "absences": break

                elif studentInfo == 3:
                    info['exam1'].append(''.join(line[studentInfo].strip(" ")))
                    if valueType == "exam1": break

                elif studentInfo == 4:
                    info['exam2'].append(''.join([x.strip(" ") for x in line[studentInfo]]))
                    if valueType == "exam2": break

                elif studentInfo == 5:
                    info['total'].append(''.join(line[studentInfo][:-1].strip(" ")))
                    if valueType == "total": break
    return info[valueType] if valueType else info # The chosen data type will be returned only



def dataSearch(data, value):

    value = value.strip(" ") # Any additional spaces at the begining or the end will be stripped
    if value.isdigit() == False:
        value = value.lower()     # In this condition we check if the value is string then we transfer all the letters into lowercase
            

    studentsInfo = studentsList() # getting all the data from the studentsList() function
    table =      """
                    -----------------------------------------------------------------------------------------------------------------
                    | id          | Name                           | Absences    | Exam1 grade    | Exam2 grade    | Total marks    |
                    |---------------------------------------------------------------------------------------------------------------|
                    """
    updatedStudentsInfo = {
            "id": [],
            "name": [],
            "absences": [],                # A new list for the searched data
            "exam1": [],
            "exam2": [],
            "total": [],
    }
    for x in [x for x in range(len(studentsInfo['id'])) if studentsInfo[data][x] == value]: # This will exclude all data expect which is searched for
        updatedStudentsInfo['id'].append(studentsInfo['id'][x])
        updatedStudentsInfo['name'].append(studentsInfo['name'][x])
        updatedStudentsInfo['absences'].append(studentsInfo['absences'][x])
        updatedStudentsInfo['exam1'].append(studentsInfo['exam1'][x])
        updatedStudentsInfo['exam2'].append(studentsInfo['exam2'][x])
        updatedStudentsInfo['total'].append(studentsInfo['total'][x])
        table += """| {} | {} | {} | {} | {} | {} |
                    -----------------------------------------------------------------------------------------------------------------
                    """.format(studentsInfo['id'][x].ljust(11), studentsInfo['name'][x].ljust(30), studentsInfo['absences'][x].ljust(11), studentsInfo['exam1'][x].ljust(14), studentsInfo['exam2'][x].ljust(14), studentsInfo['total'][x].ljust(14))
    return [table, updatedStudentsInfo]           # ljust() is for filling the value with additional spaces until it meets the length provided inside the fucntion
            # this fucntion will return data as a table that can be printed
            # and as a dictionary that can be used in the code

def dataValidate(type, value, excludeValue=""): # Additional function to make the code simpler we add all the validation into one function so we can call it anytime
    if type == 'id':                            # it has 3 parameters to choose the data type and the value that will be validated and optional parameter to exclude a value
        studentsID = studentsList('id')

        if excludeValue:
            studentsID.remove(excludeValue)     # We remove the excluded value if there is one

        errors = []
        if value in studentsID:                 # Checking if the id is duplicated
            errors.append("--- The ID is already existed ---")
        elif value.isdigit() == False:          # Checking if the id is not numbers only
            errors.append("--- The ID must contain numbers only ---")
        else:
            if len(value) != 9:                 # Checking if the length of the id is correct
                errors.append("--- Length of the ID must be equal to 9 ---")
            if int(value[:4]) < 2014 or int(value[:4]) > 2022: # First 4 numbers in the id presents the year that the student appended the university in, so if it out of the range it won't validate
                errors.append("--- The ID is not valid ---")

        if errors:
            for error in errors:
                print(error)     # Looping the errors if existed 
            return False
        else:
            return True
        
    elif type == 'name':
        errors = []
        if len(value.split(' ')) != 2:           # Checking if the name has first and last name only
            errors.append("--- The name must contain first and last name only ---")
        elif (value.split(' ')[0].isalpha() or value.split(' ')[0].isalpha()) == False:      # Checking if letters doesn't consists any numbers
            errors.append("--- The name must contain Letters only ---")
        elif len(value.split(' ')[0]) < 3 or len(value.split(' ')[1]) < 3 or len(value.split(' ')[0]) > 15 or len(value.split(' ')[1]) > 15:      # Checking if the name meets the desired range
            errors.append("--- Each first name and last name length must be between 3 and 15 ---")

        if errors:
            for error in errors:
                print(error)
            return False
        else:
            return True

    elif type == 'absences':
        errors = []
        try:
            value = int(value)
        except ValueError:
            errors.append("--- The absences must contain numbers only ---")
        else:
            if int(value) < 0 or int(value) > 60:
                    errors.append("--- The absences must be between 0 and 60 ---")

        if errors:
            for error in errors:
                print(error)
            return False
        else:
            return True
        
    elif type == 'exam':
        errors = []
        try:
            value = int(value)
        except ValueError:
            errors.append("--- The grade must contain numbers only ---")
        else:
            if int(value) < 0 or int(value) > 50:
                    errors.append("--- The absences must be between 0 and 50 ---")

        if errors:
            for error in errors:
                print(error)
            return False
        else:
            return True


def addStudent():
    isRepeat = True                                    # This variable 
    while isRepeat:
        while True:
            studentID = input("Enter the student's ID: ")
            if dataValidate("id", studentID) == True: break # validate the value by using dataValidate() function, if the validation succeed



        while True:
            studentName = input("Enter the student's name: ")
            if dataValidate("name", studentName) == True: 
                studentName = studentName.lower() # lowercase all the letters of the name
                break


        while True:
            studentAbsences = input("Enter the student's absences:")
            if dataValidate("absences", studentAbsences) == True: break



        while True:
            studentExam1 = input("Enter the student's first exam grade:")
            if dataValidate("exam", studentExam1) == True: break



        while True:
            studentExam2 = input("Enter the student's second exam grade:")
            if dataValidate("exam", studentExam2) == True: break

                                                                                                   # Adding the record with the format 
                                                                                                   # ljust() is for filling the value with spaces 
        with open("Database.txt", "a") as database:
            database.write(" | ".join([studentID.ljust(15), studentName.ljust(24), str(studentAbsences).ljust(14), str(studentExam1).ljust(14), str(studentExam2).ljust(14), str(int(studentExam1) + int(studentExam2))]) + "\n")
                                                                           
        print("--- The student has been successfully added ---")

        while True:
            isRepeat = input("Type 1 for starting again or 0 for going back:")
            if isRepeat not in ["0", "1"]:
                print("--- Wrong input ---")   # Checking if respond is within 0 and 1
            elif isRepeat == "1":
                break
            elif isRepeat == "0":
                isRepeat = False                   # Stop the repeatation 
                mainMenu()                     # returning to the main menu
                return                     # stop the current function


def removeStudent():
    isRepeat = True
    while isRepeat:
        while True:
            errors = []
            removeOption = input("Type 0, 1 to remove student by id or by name:")

            if removeOption not in ["0", "1"]:
                errors.append("--- Wrong input ---")

            elif removeOption == "0":               # Removing by id
                studentsInfo = studentsList('id')                # Geting the students' id
                studentID = input("Enter the student ID:")
                if studentID not in studentsInfo:          # Checking if students exists 
                    errors.append("--- Student does not exist ---")
                
            elif removeOption == "1":              # Removing by name
                studentsInfo = studentsList('name')              # Getting the students' name
                studentName = input("Enter the student name:")

                if studentName.lower() not in studentsInfo:      # Checking if students exists 
                    errors.append("--- Student does not exist ---") 
                else:
                    table = dataSearch('name', studentName)       # Getting all the students with the same name
                    if len(table[1]['id']) > 1:               # Checking if there're multiple students with the same name
                        print(table[0])             # print the table
                        studentOrder = input("Select the student by typing his order:")

                        try:
                            studentOrder = int(studentOrder)  # Checking if the value is int or not
                        except ValueError:
                            errors.append("--- Wrong input ---")
                        else:
                            if studentOrder < 1 or studentOrder > len(table[1]['id'])+1:    # Checking if the value meets the order
                                error.append("--- Wrong input ---")
                            else:
                                studentID = table[1]['id'][studentOrder-1]     # Getting the chosen student's id 
                    else:
                        studentID = table[1]['id'][0]     # returning the students id if there's only 1 student with same name

            
            if errors:
                for error in errors:
                    print(error)
            else:
                break

        studentRecord = dataSearch('id', studentID)
        print(studentRecord[0])

        while True:        
            confirm = input("Type 1 for removing the student or 0 canceling:")
            if confirm not in ["0", "1"]:
                print("--- Wrong input ---")             # Checking if respond is within 0 and 1

            elif confirm == "1":
                with open('Database.txt', 'r') as database:
                    lines = database.readlines()         # Read all data inside database "file"

                with open('Database.txt', 'w') as database:
                    for line in lines:
                        if line[:9] != studentID:    # Cutting the first 9 characters (the id) and compare it to the id to delete the student's data
                            database.write(line)      # Write all data except that meets the chosen student so the student will be removed
                            
                print("--- The student has been successfully removed ---")
                break
            elif confirm == "0":
                break
                        

                
        while True:
            isRepeat = input("Type 1 for starting again or 0 for going back:")
            if isRepeat not in ["0", "1"]:
                print("--- Wrong input ---")             # Checking if respond is within 0 and 1
            elif isRepeat == "1":
                break
            elif isRepeat == "0":      
                isRepeat = False        # Stop the repeatation 
                mainMenu()          # returning to the main menu
                return           # stop the current function


def edtiStudent():
    isStop = False
    while not isStop:
        errors = []
        studentID = input("Enter the student's ID:")
        table = dataSearch("id", studentID) # Getting Student's data by id

        if len(table[1]['id']) == 0:
            print("--- Student does not exist ---")

        else:
            while not isStop:
                print(table[0])         # Asking for which data type to edit
                print("""
                1- id
                2- Name
                3- Absences
                4- Exam1 grade
                5- Exam2 grade

                0- * Go back *
                """)
                options = ['id', 'name', 'absences', 'exam1', 'exam2']

                while True:
                    editOption = input("Select the field that you want to edit from the list above: ")
                    try:
                        editOption = int(editOption)
                    except ValueError:                         # Checking if the value is int
                        errors.append("--- Wrong input ---")
                    else:
                        if editOption < 0 or editOption > 5:
                            print("--- Wrong input ---")            # Checking if the value meets the inputs
                        else:
                            if editOption == 1:
                                while True:
                                    updatedID = input("Enter the new student's ID: ") # The new id
                                    if dataValidate("id", updatedID, studentID) == True: # Validate the id
                                        updatedInfo = {
                                            'id': updatedID,    # The updated data
                                            'name': table[1]['name'][0],                          # Update the student's data to a new list
                                            'absences': table[1]['absences'][0],
                                            'exam1': table[1]['exam1'][0],
                                            'exam2': table[1]['exam2'][0],
                                            'total': str(int(table[1]['exam1'][0]) + int(table[1]['exam2'][0])),
                                        }
                                        break

                            elif editOption == 2:
                                while True:
                                    updatedName = input("Enter the new student's name: ")
                                    if dataValidate("name", updatedName) == True:
                                        updatedInfo = {
                                            'id': table[1]['id'][0],
                                            'name': updatedName.lower(),    # The updated data
                                            'absences': table[1]['absences'][0],                          # Update the student's data to a new list
                                            'exam1': table[1]['exam1'][0],
                                            'exam2': table[1]['exam2'][0],
                                            'total': str(int(table[1]['exam1'][0]) + int(table[1]['exam2'][0])),
                                        }
                                        break

                            elif editOption == 3:
                                while True:
                                    updatedAbsences = input("Enter the new student's absences: ")
                                    if dataValidate("absences", updatedAbsences) == True:
                                        updatedInfo = {
                                            'id': table[1]['id'][0],
                                            'name': table[1]['name'][0],                          # Update the student's data to a new list
                                            'absences': updatedAbsences,    # The updated data
                                            'exam1': table[1]['exam1'][0],
                                            'exam2': table[1]['exam2'][0],
                                            'total': str(int(table[1]['exam1'][0]) + int(table[1]['exam2'][0])),
                                        }
                                        break

                            elif editOption == 4:
                                while True:
                                    updatedExam1 = input("Enter the new student's first exam grade: ")
                                    if dataValidate("exam", updatedExam1) == True:
                                        updatedInfo = {
                                            'id': table[1]['id'][0],
                                            'name': table[1]['name'][0],                          # Update the student's data to a new list
                                            'absences': table[1]['absences'][0],
                                            'exam1': updatedExam1,    # The updated data
                                            'exam2': table[1]['exam2'][0],
                                            'total': str(int(updatedExam1) + int(table[1]['exam2'][0])),
                                        }
                                        break                                   

                            elif editOption == 5:
                                while True:
                                    updatedExam2 = input("Enter the new student's second exam grade: ")
                                    if dataValidate("exam", updatedExam2) == True:
                                        updatedInfo = {
                                            'id': table[1]['id'][0],
                                            'name': table[1]['name'][0],                          # Update the student's data to a new list
                                            'absences': table[1]['absences'][0],
                                            'exam1': table[1]['exam1'][0],
                                            'exam2': updatedExam2,    # The updated data
                                            'total': str(int(table[1]['exam1'][0]) + int(updatedExam2)),
                                        }
                                        break
                            elif editOption == 0:    # Going back
                                isStop = True
                                mainMenu()  # Returning to the main menu
                                return

                            with open('Database.txt', 'r') as database:
                                lines = database.readlines()

                            with open('Database.txt', 'w') as database:
                                for line in lines:
                                    if line[:9] != studentID:     # Cutting the first 9 characters (the id) and compare it to the id to edit the student's data
                                        database.write(line)             
                                    else:
                                        database.write(" | ".join([updatedInfo['id'].ljust(15), updatedInfo['name'].ljust(24), str(updatedInfo['absences']).ljust(14), updatedInfo['exam1'].ljust(14), updatedInfo['exam2'].ljust(14), updatedInfo['total'] + "\n"]))
                                                                                                                 # add the edited data
                            print("--- The student's information has been successfully updated ---")

                            table = dataSearch("id", updatedInfo['id']) # Updating the table so it can be printed with the new updated data in the beginning of the loop
                        break


def top10():
    studentsInfo = studentsList() # getting all the data from the studentsList() function
    table =           """
                        -----------------------------------------------------------------------------------------------------------------
                        | id          | Name                           | Absences    | Exam1 grade    | Exam2 grade    | Total marks    |
                        |---------------------------------------------------------------------------------------------------------------|
                        """
    updatedStudentsInfo = {
            "id": [],
            "name": [],
            "absences": [],                # A new list for the top students' data
            "exam1": [],
            "exam2": [],
            "total": [],
    }

    counter = 0                           # Set a counter to limit the students to 10 only
    for grade in reversed(range(101)):
        for x in [x for x in range(len(studentsInfo['id'])) if studentsInfo['total'][x] == str(grade)]: # This will exclude all data expect which is searched for
            counter += 1
            table += """| {} | {} | {} | {} | {} | {} |
                        -----------------------------------------------------------------------------------------------------------------
                        """.format(studentsInfo['id'][x].ljust(11), studentsInfo['name'][x].ljust(30), studentsInfo['absences'][x].ljust(11), studentsInfo['exam1'][x].ljust(14), studentsInfo['exam2'][x].ljust(14), studentsInfo['total'][x].ljust(14))
                
            if counter == 10:
                break
        if counter == 10:          # If the number of students reached 10 both loops will stop
            break

    print(table)  # printing the table that shows the top 10 students

    while True:
        doReturn = input("Type 0 for going back:")
        if doReturn != "0":
            print("--- Wrong input ---")
        elif doReturn == "0":
            mainMenu()
            return

def mostAbsences():
    studentsAbsecnes = studentsList("absences") 
    studentsAbsecnes = list(map(int, studentsAbsecnes)) # Changing the data type for each value inside the list into int
    studentsAbsecnes.sort(reverse=True) # Sorting the absences from the lowest to the highest
    
    table = dataSearch("absences", str(studentsAbsecnes[0]))  # Get the students with the highest absences
    print(table[0])
    
    while True:
        doReturn = input("Type 0 for going back:")
        if doReturn != "0":
            print("--- Wrong input ---")
        elif doReturn == "0":
            mainMenu()
            return

def mainMenu(): # This is the main fucntion which enable the user to access all the other fucntions 
    while True:
        print("""
        1- Add a new student                   2- Remove a student
        3- Edit student's information          4- show top 10 students
        5- Students with Most absences         6- Exit
        
        """)
        chosenOption = input("Choose the process you want by typing the order from the list above: ")
        try:
            chosenOption = int(chosenOption)
        except ValueError:
            print("--- Wrong input ---")
        else:
            if chosenOption < 1 or chosenOption > 6:
                print("--- Wrong input ---")
            else:
                if chosenOption == 1:
                    addStudent()
                    break
                elif chosenOption == 2:
                    removeStudent()
                    break
                elif chosenOption == 3:
                    edtiStudent()
                    break
                elif chosenOption == 4:
                    top10()
                    break
                elif chosenOption == 5:
                    mostAbsences()
                    break
                elif chosenOption == 6:
                    break

mainMenu()