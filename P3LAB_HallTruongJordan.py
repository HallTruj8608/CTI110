# P3LAB_HallTruongJordan

def calculate_change(amount):
    amount_in_cents = int(round(amount * 100))  # Convert dollars to cents
    
    denominations = {
        "Dollar": 100,
        "Quarter": 25,
        "Dimes": 10,
        "Nickels": 5,
        "Pennie": 1
    }
    
    change = {}
    for name, value in denominations.items():
        count = amount_in_cents // value
        if count:
            change[name] = count
            amount_in_cents -= count * value
    
    return change

def display_change(change):
    if not change:
        print("No Change")
    else:
        for name, count in change.items():
            print(f"{count} {name}{'s' if count > 1 else ''}")

def main():
    amount = float(input("Enter the amount of money as a float: $"))
    change = calculate_change(amount)
    display_change(change)

if __name__ == "__main__":
    main()
