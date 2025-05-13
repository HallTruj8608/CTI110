# Jordan Hall-Truong
# April 5, 2025
# P4HW2
# Calculates gross pay for multiple employees
#              



total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    emp_name = input("Enter employee's name or \"Done\" to terminate: ")
    
    if emp_name == "Done":
        break

    hours_worked = float(input(f"How many hours did {emp_name} work? "))
    pay_rate = float(input(f"What is {emp_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    print("\nEmployee name:\t", emp_name)
    print("\nHours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("-------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<.2f}")
    print()

print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
