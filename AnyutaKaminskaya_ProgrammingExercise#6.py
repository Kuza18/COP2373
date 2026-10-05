# Importing regular-expression package.
import re

# - The following 3 functions use regular expressions to match the user's input
#   to a defined pattern for their Phone Number, SSN, and Zip Code -

# Phone Number
def get_phone_number():
    pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d'
    # Loop asking user for valid phone number.
    while True:
       phone = input('Enter your phone number: ')
       # Match input to defined pattern using re.
       if re.fullmatch(pattern, phone):
          print('Number accepted.')
          return phone
       else:
          print('Incorrect format.')
          continue

# SSN
def get_ssn():
   pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d'
   # Loop asking user for valid ssn.
   while True:
      ssn = input('Enter your ssn: ')
      # Match input to defined pattern using re.
      if re.fullmatch(pattern, ssn):
         print('Number accepted.')
         return ssn
      else:
         print('Incorrect format.')
         continue

# Zip Code
def get_zip_code():
   pattern = r'\d\d\d\d\d[ -]\d\d\d\d'
   # Loop asking user for valid zip code.
   while True:
      code = input('Enter your zip code: ')
      # Match input to defined pattern using re.
      if re.fullmatch(pattern, code):
          print('Number accepted.')
          return code
      else:
         print('Incorrect format.')
         continue

# - END of functions using regular expressions -


# Gives directions to user and calls all functions.
def main():
   print('- Please enter:\n'
         '- phone number(xxx-xxx-xxxx),\n'
         '- SSN(xxx-xx-xxxx),\n'
         '- zip code (xxxxx-xxxx)\n'
         '- when prompted to verify it is valid')
   print(" ")
   phone = get_phone_number()
   ssn = get_ssn()
   code = get_zip_code()
   print (" ")
   print(f"Congrats! All of your information is valid!\n"
         f" Phone#:({phone})\n"
         f" SSN:({ssn})\n"
         f" Zip Code:({code})")

main()