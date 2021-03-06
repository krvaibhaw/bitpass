
'''

Bitpass Test File 
Randomly generates 101 passwords of 20 characters long

'''

import string
import random

def passwordgen(n):

    
    slot = [0, 0, 0, 0, 0]
    
    for x in range(n):
        r = random.randint(0,4)
        slot[r] += 1
    
    lower_letter = random.choices(string.ascii_lowercase, k=slot[0])
    upper_letter = random.choices(string.ascii_uppercase, k=slot[1])
    digits = random.choices(string.digits, k=slot[3])
    symbols = random.choices('!@#$%^&*_+-|/[]}{><?:",.', k=slot[2])
    symbols2 = random.choices('!@#$%^&*_+-|/[]}{><?:",.', k=slot[4])    
    
    password = digits + upper_letter  + symbols + lower_letter + symbols2
    random.shuffle(password)
    
    print(''.join(password))


def main():
    
    #n = int(input('Enter total number of characters : '))

    for i in range(101):
        passwordgen(20)
        
if __name__ == "__main__":
    main()
