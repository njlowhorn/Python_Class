
class Employee():
    def __init__(self, name, age, town, empID, payRate, deductions):
        self.name = name
        self.age = int(age)
        self.town = town
        self.empID = empID
        self.payRate = float(payRate)
        self.deductions = float(deductions)
        self.next = None

    def pay(self, hours):
        if hours <= 40:
            gross = hours * self.payRate
        else:
            gross = 40 * self.payRate + (hours - 40) * self.payRate * 1.5
        self.deductions = self.deductions / 100
        witholding = gross * self.deductions
        net = gross - witholding
        return print(self.name + f": gross pay: ${gross:.2f} deductions: ${witholding:.2f} final pay: ${net:.2f}")

    def push(self, head, empl):
        if head.next == None:
            head.next = empl
        else:
            self.push(head.next, empl)

    def pop(self, head):
        if head.next.next == None:
            top = head.next
            head.next = None
            hours = float(input(f"How many hours did {top.name} work? "))
            return top.pay(hours)
        else:
            self.pop(head.next)
