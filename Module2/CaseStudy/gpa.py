# Python V 3.9.0
# Nolan Lowhorn
# gpa.py
# Program that checks if a student has made the Honor Roll or the Dean's List based on their GPA

last_name = input("Enter the student's last name: ")

if last_name == "ZZZ":
    print("Sorry, couldn't process")
else:
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's list.")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll.")
    else:
        print(first_name + " " + last_name + " hasn't made the Honor Roll or the Dean's List.")

