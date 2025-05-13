# Jordan Hall-Truong
# 3/26/2025
# P3HW2
# The program calculates an employee's total pay.



# Pseudocode:

# 1. Ask user to enter employee's name

# 2. Ask user to enter number of hours worked

# 3. Ask the user to enter the employee's pay rate

# 4. Determine if the employee worked overtime

# 5. If overtime exists, calculate overtime hours and pay

# 6. Calculate regular pay

# 7. Compute gross pay

# 8. Display results




employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

overtime_rate = 1.5
regular_hours = 40

if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * (pay_rate * overtime_rate)
else:
    overtime_hours = 0
    overtime_pay = 0

regular_pay = min(hours_worked, regular_hours) * pay_rate

gross_pay = regular_pay + overtime_pay

print("-" * 50)
print(f"Employee name:\t{employee_name}")
print("\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-" * 50)
print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")
