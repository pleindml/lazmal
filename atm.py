balance = 0

while True:
    print("\nOptions:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        amount = float(input("Enter deposit amount: $"))
        balance += amount
        print(f"${amount} deposited successfully.")
        print(f"Your current balance is: ${balance}")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: $"))
        if balance >= amount:
            balance -= amount
            print(f"${amount} withdrawn successfully.")
            print(f"Your current balance is: ${balance}")
        else:
            print(f"Insufficient funds. Your current balance is ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
