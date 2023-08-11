def calculate_ticket_price(age):
    if age < 5:
        return 0
    elif age >= 5 and age <= 18 or age >= 65:
        return 20
    else:
        return 30

def main():
    try:
        age = int(input("Please enter your age: "))
        ticket_price = calculate_ticket_price(age)
        print("The ticket price is:", ticket_price)
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()
