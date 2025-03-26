

 # Jordan Hall-Truong
 # 3/3/25
 # P1HW2
 # Travel Expenses



print("This program calculates and displays travel expenses")
budget = float(input("Enter your budget for the trip: $"))
destination = input("Enter your travel destination: ")
gas_expenses = float(input("Enter the amount you will spend on gas: $"))
accommodation_expenses = float(input("Enter the amount you will spend on accommodation: $"))
food_expenses = float(input("Enter the amount you will spend on food: $"))

# Calculating total expenses
total_expenses = gas_expenses + accommodation_expenses + food_expenses

# Calculating remaining budget
remaining_budget = budget - total_expenses

# Displaying the results
print("-----Your Travel Expenses-----")
print(f"\nYour travel destination: {destination}")
print(f"How much will you spend on gas: ${gas_expenses}")
print(f"Your total expenses on accommodation: ${accommodation_expenses}")


print(f"Your total expenses on food: ${food_expenses}")
print(f"Your total expenses: ${total_expenses}")
print(f"Your remaining budget after expenses: ${remaining_budget}")
