import functools

def get_expenses():
    print('------ Monthly Expenses Analyzer ------')
    print('Calculates the following with your monthly expenses: [total] [lowest] [highest]')
    print("Just enter your expense and it's amount when prompted." )
    print('------------------------------------------------------------------------------------')

    expenses = []
    while True:
        kind = input('Enter the expense type: ')
        if not kind.strip():
            print('ERROR!')
            continue
        if kind.isdigit():
            print('ERROR!: You entered the amount!')
            continue

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

        expenses.append((kind, amount))
        while True:
            proceed = input('Are you finished? [y/n]: ')
            if proceed.lower() in ['n', 'no']:
                break
            if proceed.lower() in ['y', 'yes']:
                return expenses
        continue

def main():
    expenses = get_expenses()


    amounts = [amount for kind, amount in expenses]

    total = functools.reduce(lambda x, y: x + y, amounts)
    highest = functools.reduce(lambda a, b: a if a[1] >= b[1] else b, expenses)
    lowest = functools.reduce(lambda a, b: a if a[1] <= b[1] else b, expenses)

    print(f'\nTotal expenses: ${total:.2f}')
    print(f'Highest expenses: {highest[0]} at ${highest[1]:.2f}')
    print(f'Lowest expense: {lowest[0]} at ${lowest[1]:.2f}')


main()
