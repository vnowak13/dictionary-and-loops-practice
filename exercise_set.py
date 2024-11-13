import student_data

# Step 1: Print Student Details
student = student_data.students
for student in student:
    print(student['Combo,Name'])
    print(student['Email'][0])
    print(student['Email'][1]) 
    print("_"*36)

#Step 2: Search for Students in a Specific Homeroom
homeroom_code = input("Enter a homeroom code: ")
for student in student_data.students:
    if homeroom_code == student['HR']:
        print(student['Combo,Name'])
        print(student['Email'][0])
        print(student['Email'][1])
if homeroom_code != student['HR']:
        print("No students found in this homeroom.")

# Step 3: Check if a Student is in a List
name  = input("Enter your first name:")
for name in student['Combo, Name']:
    print(student['Combo, Name'])
    print(student['HR'])

#step 4 Filter Students by Grade Level
print("Grade 10 Students:")
for student in student_data.students:
    if student['GL'] == 10:
        print(student['Combo,Name'])

#step 5: Format Email List for Newsletter


# Step 6: Find and print common last names
last_names = {}
for student in student_data.students:
    last_name = student['LName']
    last_names[last_name] = last_names.get(last_name, []) + [student['Combo,Name']]

print("Common Last Names:")
for last_name, names in last_names.items():
    if len(names) > 1:
        print(f"{last_name}: {', '.join(names)}")
 