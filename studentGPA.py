# Author: Minh Tong
# File Name: studentGPA.py
# Description: A python that will help the student know if they qualify for Dean's List or Honor Roll 
last_name = "a"
while last_name != "ZZZ":
    last_name = input("Please Enter Student's Last Name or Enter 'ZZZ' to quit the program: ")
    if last_name == "ZZZ":
        break
    first_name = input("Please Enter Student's First Name: ")

    #while loop to see if the student type in the valid GPA or not.

    gpa_grade = float(input("Please Enter Student's GPA: "))
    while 0.0 > gpa_grade or gpa_grade > 4.0:
        print("Invalid GPA! Please enter a value between 0.0 and 4.0.")
        gpa_grade = float(input("Please Enter Student's GPA: "))

    #if statement to calculate and see which award the student is qualify.

    if gpa_grade >= 3.5:
        print("Congratulations, student " + first_name + " " + last_name + " made the Dean's List!")
    elif gpa_grade >= 3.25:
        print("Congratulations, student " + first_name + " " + last_name + " made the Honor Roll!")
    else:
        print("Sorry, student " + first_name + " " + last_name + " did not qualify for any awards.")

print("Program Exited")
