
from paycheck import employee
import csv

boss = employee.Employee("bossman", 40, "town", 1121, 0.00, 0.00)

with open("workforce.csv", "r") as fromFile:
    reader = csv.reader(fromFile)
    for row in reader:
        if len(row) != 0:
            temp = employee.Employee(row[0], row[1], row[2], row[3], row[4], row[5])
            boss.push(boss, temp)

while boss.next != None:
    boss.pop(boss)

