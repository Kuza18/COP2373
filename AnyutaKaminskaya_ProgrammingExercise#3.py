import functools

# Takes in user input and checks for user error. Returns user input as pairs in a list.
def get_expenses():
    print('------ Monthly Expenses Analyzer ------')
    print('Calculates the following with your monthly expenses: [total] [lowest] [highest]')
    print("Just enter your expense and it's amount when prompted." )
    print('------------------------------------------------------------------------------------')

    # Creating initial empty list to be filled.
    expenses = []

    # 1st While loop Takes expense type and checks for user error.
    while True:
        kind = input('Enter the expense type: ')
        if not kind.strip():
            print('ERROR!')
            continue
        if kind.isdigit():
            print('ERROR!: You entered the amount!')
            continue

        # 2nd While loop takes the amount and checks for user error.
        while True:
            try:
                amount = float(input(f'Enter the monthly expense for {kind}: $'))
            except ValueError:
                print('ERROR!')
                continue
            if amount < 0:
                print('ERROR!: A negative value is not valid, try again.')
                continue
            else:
                break

        # Expense kind and amount is added to the end of expenses list as a tuple.
        expenses.append((kind, amount))

        # 4th While loop to ask user if they are done and checks for user error.
        # If yes then the final list is returned, if not, the loop restarts.
        while True:
            proceed = input('Are you finished? [y/n]: ')
            if proceed.lower() in ['n', 'no']:
                break
            if proceed.lower() in ['y', 'yes']:
                return expenses
        continue

# main() function calculates the total, highest, and lowest, expenses from user input.
def main():
    # Calls function that asks user for their expenses,
    # giving a list of tuples.
    expenses = get_expenses()

    # Go through that list and pull out only the expense amount,
    # putting them in their own list.
    amounts = [amount for kind, amount in expenses]

    # Add the amounts together two at a time until one number is left.
    # x is the running total so far, y is the next amount.
    total = functools.reduce(lambda x, y: x + y, amounts)

    # Compare the pairs two at a time and keep whichever has the bigger amount.
    highest = functools.reduce(lambda a, b: a if a[1] >= b[1] else b, expenses)
    # Same process but keeps the lowest amount.
    lowest = functools.reduce(lambda a, b: a if a[1] <= b[1] else b, expenses)

    # Print the total. \n adds a blank line first, and :.2f shows two decimals.
    print(f'\nTotal expenses: ${total:.2f}')
    # Print the highest. [0] is the name, [1] is the amount.
    print(f'Your Highest expense was: {highest[0]} at ${highest[1]:.2f}')
    # Prints the lowest
    print(f'While your Lowest expense was: {lowest[0]} at ${lowest[1]:.2f}')


main()
