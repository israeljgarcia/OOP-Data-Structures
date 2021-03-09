class CheckingAccount:
    def __init__(self, starting_balance, num_checks):
        if starting_balance < 0:
            raise BalanceError("The starting balance cannot be below zero.")
        self.balance = starting_balance
        self.check_count = num_checks

    def deposit(self, amount):
        self.balance += amount

    def write_check(self, amount):
        if self.balance - amount < 0:
            raise BalanceError("Check amount cannot exceed balance amount.")

        if self.check_count == 0:
            raise OutOfChecksError("Insufficient checks.")
        self.balance -= amount
        self.check_count -= 1

    def display(self):
        print(f'Balance: {self.balance}\nChecks: {self.check_count}')

    def apply_for_credit(self, amount):
        pass


class BalanceError(Exception):
    def __init__(self, message):
        # Don't forget to pass the message to the base class
        super().__init__(message)


class OutOfChecksError(Exception):
    def __init__(self, message):
        super().__init__(self, message)


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))

            acc = CheckingAccount(balance, num_checks)
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            amount = float(input("Amount: "))
            acc.write_check(amount)
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()
