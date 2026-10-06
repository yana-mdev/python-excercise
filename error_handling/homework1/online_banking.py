class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


PIN_code, initial_balance, age = input().split(", ")
PIN_code, age = int(PIN_code), int(age)
initial_balance = float(initial_balance)

while True:
    command = input()
    if command == "End":
        break

    action, money, *pin_code = command.split("#")
    money = float(money)
    pin_code = int(pin_code[0] if pin_code else 0)

    if action == "Send Money":
        if money > initial_balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if PIN_code != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        initial_balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {initial_balance:.2f} money left in the bank account")
    elif action == "Receive Money":
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        initial_balance += (money/2)
        print(f"{(money/2):.2f} money went straight into the bank account")


