def mostrar_menu():
    print("""
  Please, select an option:

  1 - Statement
  2 - Withdraw
  3 - Deposit
  4 - Exit
""")

def mostrar_extrato(statement, balance):
    print("********************* Bank Statement *********************")
    print(statement if statement else "No transactions recorded.")
    print(f'Balance: $ {balance:.2f}')
    print("**********************************************************")

def sacar(balance, limit, num_withdraws, max_withdraws, statement):
    try:
        valor = float(input("Please, enter the withdraw value: "))
        if valor <= 0:
            print("❌ Invalid value! Must be greater than zero.")
        elif num_withdraws >= max_withdraws:
            print(f"❌ Withdraw limit reached: {max_withdraws} per day.")
        elif valor > limit:
            print(f"❌ Exceeds per-operation limit of $ {limit:.2f}")
        elif valor > balance:
            print("❌ Insufficient funds.")
        else:
            balance -= valor
            statement += f'Withdraw: $ {valor:.2f}\n'
            num_withdraws += 1
            print(f"✅ Withdraw completed. You have used {num_withdraws} of {max_withdraws} withdrawals.")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

    return balance, num_withdraws, statement

def depositar(balance, statement):
    try:
        valor = float(input("Please, enter the deposit value: "))
        if valor <= 0:
            print("❌ Invalid value! Must be greater than zero.")
        else:
            balance += valor
            statement += f'Deposit: $ {valor:.2f}\n'
            print("✅ Deposit successful!")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

    return balance, statement

# Inicialização
balance = 0.0
limit = 500.0
num_withdraws = 0
max_withdraws = 3
statement = ""

# Loop principal
while True:
    mostrar_menu()
    try:
        option = int(input("Your choice: "))
    except ValueError:
        print("❌ Invalid option! Please enter a number between 1 and 4.")
        continue

    if option == 1:
        mostrar_extrato(statement, balance)

    elif option == 2:
        balance, num_withdraws, statement = sacar(balance, limit, num_withdraws, max_withdraws, statement)

    elif option == 3:
        balance, statement = depositar(balance, statement)

    elif option == 4:
        print("👋 Thank you for using our banking system. Goodbye!")
        break

    else:
        print("❌ Invalid option! Please select a valid one.")
