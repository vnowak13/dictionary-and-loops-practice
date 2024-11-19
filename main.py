# # Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data
# # print(student_data.students)
students = student_data.students
# # print(len(students))
# # print(students[4]['Combo,Name'])
# # print(students[4]['Email'][0])
# # print(students[4]['Email'][1])

# # for loops allow us to
# #iterate through the data
# #and perform some function

# #we are iterating through the data
# #and printing the name and email of the students
# #we are also printing a line of underscores to separate the students
# #we are also printing a line of underscores to separate the students
# # for student in students:
# #    print(student['Combo,Name'])
# #    print(student['Email'][0])
# #    print(student['Email'][1])
# #    print(student['HR'])
# #    print(student['GL'])
# #    print("_"*25)


# # we are asking the user to input their name
# # then we are checking if the name is in the data
# # if the name is in the data we are printing the name and "this works"
# id = int(input("what is you id number? "))
# for student in students:
#     if id == student['CPSID']:
#         print(student['CPSID'])
#         print("this works")


# # Let's try to print out the emails of the students:    

# Example: Updating a student's first name in a list of student dictionaries
for student in students:
    if student['CPSID'] == 10000011:  # Replace with the condition to find the specific student
        student['FName'] = 'Victoria'  # Update the first name
        student['LName'] = 'Nowak'   # Update the last name
        print(f"Updated student: {student}")

for student in students:
    if student['CPSID'] == 10000012:  # Replace with the condition to find the specific student
        del student['MName']  # Deletes the 'MName' key-value pair
        print(f"Updated student: {student}")

for student in students:
    if student['CPSID'] == 10000013:  # Replace with the condition to find the specific student
        del student['MName']  # Deletes the 'MName' key-value pair
        print(f"Updated student: {student}")

# Using a loop to find and remove a student by a specific condition
students = [student for student in students if student['CPSID'] != 10000014]  # Keeps all except the one with CPSID 123456

# Update a specific entry by index
students[0]['FName'] = 'Angela'  # Updates the first student's first name
students[0]['LName'] = 'Macias'
print(students[0])

# Remove a specific student by index
del students[8]  # Removes the first student in the list

# Example: Add a 'ContactNumber' field to each student
for student in students:
    student['ContactNumber'] = '123-456-7890'  # Assign a default or specific value
#######################################################################################
# Create a new student dictionary
new_student = {
    'CPSID': 10000047,
    'Combo,Name': 'Doe, John',
    'FName': 'John',
    'LName': 'Doe',
    'MName': 'Paul',
    'HR': 'B220',
    'GL': 11,
    'Email': ['john.doe@example.com', 'j.doe@example.org']
}
# Add the new student to the list
students.append(new_student)
#######################################################################
# Collecting input from the user for each field
cpsid = int(input("Enter CPSID: "))
combo_name = input("Enter Combo,Name (Last, First): ")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
middle_name = input("Enter Middle Name: ")
homeroom = input("Enter Homeroom (e.g., B220): ")
grade_level = int(input("Enter Grade Level: "))
primary_email = input("Enter Primary Email: ")
secondary_email = input("Enter Secondary Email: ")

# Create a new student dictionary using the input
new_student = {
    'CPSID': cpsid,
    'Combo,Name': combo_name,
    'FName': first_name,
    'LName': last_name,
    'MName': middle_name,
    'HR': homeroom,
    'GL': grade_level,
    'Email': [primary_email, secondary_email]
}

# Add the new student to the list
students.append(new_student)

# Print confirmation and the new student details
print("New student added:")
print(new_student)
#############################################################################

# Overwrite the `student_data.py` file with the updated data
with open('student_data.py', 'w') as f:
    f.write("students = [\n")
    for student in students:
        f.write(f"    {repr(student)},\n")  # Use repr() to write the dictionary as a string suitable for Python code
    f.write("]\n")

print("student_data.py has been updated.")
