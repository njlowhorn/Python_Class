
import csv

x = input("is there another employee (yes/no): ")
while x.lower() == "yes":
    name = input("enter name: ")
    age = int(input("enter age: "))
    town = input("enter town: ")
    empID = input("enter last four digits of social: ")
    payRate = float(input("enter the pay rate: "))
    deductions = float(input("enter the % of witholdings as a %: "))

    with open("workforce.csv", "a") as toFile:
        writer = csv.writer(toFile)
        writer.writerow([name, age, town, empID, payRate, deductions])
    x = input("is there another employee (yes/no): ")

if __name__ == "__main__":
    pass
