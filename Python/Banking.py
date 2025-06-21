def show_menu():
    print("""
Please select an option:

1 - View Statement
2 - Make a Withdrawal
3 - Make a Deposit
4 - Exit
""")

def show_statement(statement, balance):
    print("******************** BANK STATEMENT ********************")
    if statement:
        print(statement)
    else:
        print("No transactions recorded.")
    print(f"Current Balance: $ {balance:.2f}")
    print("*******************************************************")

def perform_withdrawal(balance, limit, withdrawals_made, max_withdrawals, statement):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("❌ Invalid amount! Please enter a positive value.")
        elif withdrawals_made >= max_withdrawals:
            print(f"❌ Withdrawal limit reached: maximum of {max_withdrawals} withdrawals allowed.")
        elif amount > limit:
            print(f"❌ Amount exceeds the per-transaction limit of $ {limit:.2f}.")
        elif amount > balance:
            print("❌ Insufficient balance.")
        else:
            balance -= amount
            statement += f"Withdrawal: $ {amount:.2f}\n"
            withdrawals_made += 1
            print(f"✅ Withdrawal successful. You have used {withdrawals_made}/{max_withdrawals} withdrawals.")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

    return balance, withdrawals_made, statement

def perform_deposit(balance, statement):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("❌ Invalid amount! Please enter a positive value.")
        else:
            balance += amount
            statement += f"Deposit: $ {amount:.2f}\n"
            print("✅ Deposit successful!")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

    return balance, statement

# Initialization
balance = 0.0
withdrawal_limit = 500.0
withdrawals_made = 0
max_withdrawals = 3
statement = ""

# Main loop
while True:
    show_menu()
    try:
        option = int(input("Your choice: "))
    except ValueError:
        print("❌ Invalid choice! Please ente
