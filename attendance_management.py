teacher_name = input("enter the name of the teacher")
list_of_names = []
teacher_choice = int(input("what you want to do \n1.Mark Attendance \n2.Quit"))
if teacher_choice == 1:
    num_of_students = int(input("enter the number of students"))
    while num_of_students > 0:
        num_of_students = num_of_students - 1
        student_name = input("enter the name of the student")
        check_existence = student_name in list_of_names
        if check_existence:
            sure = input("are you sure.say in yes or no")
            if sure == 'yes':
                list_of_names.append(student_name)
            else:
                student_name = input("enter the name of the student")
                list_of_names.append(student_name)

        else:
            list_of_names.append(student_name)
elif teacher_choice == 2:
    print("bye")
else:
    print("wrong choice")
for name in list_of_names:
    print(name)
