
'''

Bitpass Password Generator

A password generator utility which utilizes the slot technique
to generate strong passwords of required length having combinations
of lower and upper characters, digits and symbols.

'''


# Importing libraries

import string
import random


# Bitpass generator function

def bitpass(n):


    # Defining slots for each sub section of password
    # containing ower and upper characters, digits and symbols.

    slot = [0, 0, 0, 0, 0]

    
    for x in range(n):

        # Randomly assigning slot values

        r = random.randint(0,4)
        slot[r] += 1

    
    # Defining which sub section will belong to which slots
    # with the help of slot index.

    lower_letter = random.choices(string.ascii_lowercase, k=slot[0])
    upper_letter = random.choices(string.ascii_uppercase, k=slot[1])
    digits = random.choices(string.digits, k=slot[3])
    symbols = random.choices('!@#$%^&*_+-|/[]}{><?:",.', k=slot[2])
    symbols2 = random.choices('!@#$%^&*_+-|/[]}{><?:",.', k=slot[4]) 


    # Combining the subsections to generate the password   
    
    password = digits + upper_letter  + symbols + lower_letter + symbols2
    

    # Finally suffleing the string to make the password more 
    # strong and distinct.

    random.shuffle(password)
    print(''.join(password))


def main():

    # Taking password length as input from user.
    
    n = int(input('Enter total number of characters : '))
    bitpass(n)
        
if __name__ == "__main__":
    main()
