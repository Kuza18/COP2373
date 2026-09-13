# Gets user input and checks for user error.
# Returns email.
def get_valid_email():
    # Explaining to user how it works.
    print('----------- Is Your Email Spam? -----------')
    print("--- This system scans your email for words or phrases commonly found in spam and assigns it a spam rating ---")
    print(" - The Scoring is [0-10: Not]    [10-20: Likely]    [20-30: Very Likely]    [30+: Certainly] - ")
    print(" ")

    # The following loop prompts the user for an email and checks for input error.
    while True:
        # Enters nothing.
        email = input(str('Enter a valid email here: ')).strip()
        if not email:
            print('ERROR! Your response was empty!')
            continue
        # Enters only numbers.
        if email.isdigit():
            print('ERROR! You only entered numbers!')
            continue
        # Cannot be a short sentence.
        if len(email) < 10:
            print('Your email is too short!')
            continue
        # Must contain spaces.
        if " " not in email:
            print('Your email has no spaces!')
            continue
        else:
            break
    return email

# Holds list of common spam words, reads user input for any spam word occurrence and puts them in a dictionary.
# Returns spam_caught.
def spam_check():
    # List of 30 common spam words or phrases.
    spam_words = ["winner", "free", "money", "hurry", "before it's too late", "this wont last", "click here",
                  "urgent", "no cost", "last call", "guaranteed", "cash back", "one time", "offer", "act now",
                  "limited", "bonus", "cash", "discount", "while supplies last", "you have been selected",
                  "exclusive", "apply now", "save", "million", "freedom", "make money", "friend", "investment", "miracle"]
    # Calls function to receive user's email.
    email = get_valid_email()
    # Makes all words in user's email lower case since the spam list is in lower case.
    email_lower = email.lower()

    # Dictionary holding the spam words found and value of its occurrence.
    spam_caught = {}

    # This for loop searches the user's email for any words that are in the spam_words list
    # and if detected, adds the word and its value to the spam_caught dictionary.
    for phrase in spam_words:
        count = email_lower.count(phrase)
        if count > 0:
            spam_caught[phrase] = count
    return spam_caught

# Assigns the spam score and likelihood, then prints them to user.
def main():
    # Calling function to extract the spam_caught dictionary.
    spam_caught = spam_check()
    # This loop counts and adds all values of each spam occurrence
    # and assigns the final value to total_found.
    total_found = 0
    for phrase, count in spam_caught.items():
        total_found += count

    # Spam score is the total_found with a cap of 30.
    spam_score = min(total_found, 30)

    # Assigning likelihood it is spam depending on spam score.
    if spam_score < 10:
        likelihood = 'not'
    elif spam_score < 20:
        likelihood = 'likely'
    elif spam_score < 30:
        likelihood = 'very likely'
    else:
        likelihood = 'certainly'

    # Displays to user the spam words detected, spam score, and spam likelihood.
    print("Spam Words Detected and Their Occurrences:", spam_caught)
    print('This email scored a', spam_score,'/ 30 on the spam rating so this email is', likelihood ,"spam.")

main()