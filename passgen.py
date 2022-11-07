#!/usr/bin/env python3

import random
import string

# lengh of the password
pass_l = random.randint(16,20)

password = ''  # string that will contain the generated password

while True:
    round = random.randint(0,3) # number of lowercase characters to add
    i = 0
    while i < round:
        random_low = random.choice(string.ascii_lowercase)
        password += random_low
        i += 1
        if len(password) == pass_l:
            exit(password)
    round = random.randint(0,3) # number of uppercase characters to add
    i = 0
    while i < round:
        random_up = random.choice(string.ascii_uppercase)
        password += random_up
        i += 1
        if len(password) == pass_l:
            exit(password)
    round = random.randint(0,3) # number of digits to add
    i = 0
    while i < round:
        random_int = random.randint(0,9)
        password += str(random_int)
        i += 1
        if len(password) == pass_l:
            exit(password)
    round = random.randint(0,3) # number of special characters to add
    i = 0
    while i < round:
        random_sp = random.choice(string.punctuation)
        password += random_sp
        i += 1
        if len(password) == pass_l:
            exit(password)
