
# Defines a BankAcct class that stores account information, supports deposits, withdrawals, interest rate changes,
# and interest calculation.
class BankAcct:
    # Every account uses the same number of days per year, so it belongs to the class.
    DAYS_IN_YEAR = 365

    # __init__ makes sure every account has the same set of instance variables with its own values.
    def __init__(self, name, acct_num, amount=0.0, int_rate=0.0):
        # Account holder's name
        self.name = name
        # Account #
        self.acct_num = acct_num
        # Current balance
        self.amount = amount
        #  Annual interest rate
        self.int_rate = int_rate

        # Tracks the most recent interest calculations.
        # __str__ can then display interest amount with balance.
        self.last_interest = 0.0
        self.last_days = 0

    # Changes the annual interest rate and rejects negative rates.
    def adjust_int_rate(self, new_rate):
        if new_rate < 0:
            print("Error: interest rate cannot be negative.")
        else:
            self.int_rate = new_rate
            print(f"Interest rate changed to {self.int_rate}%.")

    # Adds money to the account and only positive amounts are allowed.
    def deposit(self, dep_amt):
        if dep_amt <= 0:
            print("Error: deposit amount must be positive.")
        else:
            self.amount += dep_amt
            print(f"Deposited amount ${dep_amt:,.2f}")

    # Removes money from the account.
    # Checks for positive amount and sufficient funds.
    def withdraw(self, wd_amt):
        if wd_amt <= 0:
            print("Error: withdrawal amount must be positive.")
        elif wd_amt > self.amount:
            print(f"Error: insufficient funds to withdraw ${wd_amt:,.2f}.")
        else:
            self.amount -= wd_amt
            print(f"Withdrew ${wd_amt:,.2f}.")

    # Returns the current balance.
    def balance(self):
        return self.amount

    # Calculates simple interest earned over a number of days:
    # -----> interest = balance * (rate/100) * (days/365)
    def calc_interest(self, days):
        if days < 0:
            print("Error: number of days cannot be negative.")
            return 0.0
        interest = self.amount * (self.int_rate / 100) * (days / BankAcct.DAYS_IN_YEAR)
        self.last_interest = interest
        self.last_days = days
        return interest

    # __str__ returns a readable string showing all the account details.
    def __str__(self):
        s = f"Account #{self.acct_num} - {self.name}\n"
        s += f"  Balance: ${self.amount:,.2f}\n"
        s += f"  Interest rate: {self.int_rate}%\n"
        s += f"  Interest for {self.last_days} days: ${self.last_interest:,.2f}"
        return s

# Creates a test account and calls every method to show it works.
def test_bank_acct():
    print("=== Create Bank Account ===")
    acct = BankAcct("Anyuta", "100123", 10000.00, 2.5)
    print(acct)

    print("\n===Deposit and Withdraw ====")
    acct.deposit(500)
    acct.withdraw(200)
    print(f"Balance is now ${acct.balance():,.2f}")

    print("\n=== Error Checking ====")
    acct.deposit(-500)
    acct.withdraw(11000)
    acct.adjust_int_rate(-1)

    print("\n=== Interest for 30 days at 2.5% ===")
    acct.calc_interest(30)
    print(acct)

    print("\n=== Change rate - Interest for 90 days ===")
    acct.adjust_int_rate(3.0)
    acct.calc_interest(90)
    print(acct)

# Runs the test account
def main():
    test_bank_acct()

# Only runs main() when this file is run directly and not when imported into another file.
if __name__ == "__main__":
    main()
