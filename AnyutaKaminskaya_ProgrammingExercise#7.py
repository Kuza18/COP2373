# Importing regular-expression package.
import re

# Asks user for a paragraph and compares it with a pattern
# that identifies each sentence in it.
def sentence_counter():

    # Checks for basic input errors such as entering:
    # nothing, space, and only numbers.
    while True:
        paragraph = input('Please enter your paragraph: ')
        if any(char.isalpha() for char in paragraph):
            break
        print('ERROR')

    # Pattern used to read all periods at the end of an actual sentence.
    # The sentence has to start with a space and capitol letter or number.
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    # Scans the paragraph to collect all text that matches the pattern
    # and puts everything found into a list.
    m = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    return m

# Calls all functions and then tells user the amount of sentences
# in the paragraph and displays each one.
def main():
    # Calling function.
    m = sentence_counter()

    print(" ")
    # len(m) counts how many items/sentences are in the list m.
    print(f"There are {len(m)} sentences in your paragpraph.")
    print("Here they are: ")
    # prints each sentence in the list m.
    for i in m:
        print('->', i)

main()