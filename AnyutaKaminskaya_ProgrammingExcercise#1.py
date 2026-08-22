
# Defining buy_tick() function with parameters
# to ensure limited amount of tickets and buyers are set to 0.
def buy_tick(tick_available, buyers):
    print('Hurry! Only 20 cenima tickets remain! Buy up to 4 tickets at a time!')

    # Creating While loop so user is prompted until tickets are sold out.
    while 1 <= tick_available <= 20:

        # The next few lines of code will be testing for User Error:
        # User enters a space.
        try:
            user_input = int(input('How many tickets would you like to buy?: '))
        except ValueError:
            print("ERROR: Please enter the amount of tickets you would like to buy.")
            continue

        # User cannot buy out of the buyer range which is 1-4 tickets.
        if user_input > 4:
            print("ERROR: You can buy 4 tickets at a time.")
            continue

        # User can't enter 0 or a negative number.
        elif user_input <= 0:
            print("ERROR: Try again.")
            continue

        # User can't buy more tickets than what is available.
        elif user_input > tick_available:
            print(f"ERROR: Only {tick_available} tickets remaining")
            continue

        # When user passes these tests:
        # tick_available is subtracted from user_input and reassigned
        # to the new value
        # count() is called to add 1 to buyers.
        else:
            tick_available -= user_input
            buyers = count(buyers)
            print(f'{tick_available} cenima tickets remaining!')

    # When loop ends, the user is notified that they cannot buy anymore and
    # the number of buyers is stated.
    print(f'Sorry we sold out! Total Buyers: {buyers}.')

# Defining count() function with parameters so buyers start off as 0
def count(buyers):
    # One is added to buyers each time function is called
    buyers += 1
    # The integer assigned to buyers is returned so it can be used when called.
    return buyers

# Calling function and assigning data to tick_available and buyer.
buy_tick(20, 0)


