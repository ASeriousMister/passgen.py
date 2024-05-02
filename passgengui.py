#!/usr/bin/env python3

import random
import string
import tkinter as tk
import pyperclip


def close_window():
    pyperclip.copy('')  # Clear the clipboard
    window.destroy()
    

def pop_up_show(password):
#    window = tk.Tk()
    window.title("Random password")
    window.configure(bg="dark grey")

    label = tk.Label(window, text=password, fg="light blue", bg="black", padx=10, pady=10)
    label.pack(padx=10, pady=10)

    copy_button = tk.Button(window, text="Copy to Clipboard", command=pyperclip.copy(password))
    copy_button.pack(padx=10, pady=10)

    close_button = tk.Button(window, text="Close X", command=close_window)
    close_button.pack(padx=10, pady=10)

    window.mainloop()


# lengh of the password
pass_l = random.randint(16,20)

password = ''  # string that will contain the generated password
window = tk.Tk()

# Variables that check if all requisites are satisfied
low_c = False
up_c = False
dig_c = False
sym_c = False

while True:
    round = random.randint(0,3) # number of lowercase characters to add
    i = 0
    if round > 0 and low_c is False:
        low_c = True
    while i < round:
        random_low = random.choice(string.ascii_lowercase)
        password += random_low
        i += 1
        if len(password) == pass_l:
            if low_c and up_c and dig_c and sym_c:
                pop_up_show(password)
                exit()
            else:
                password = ''
                low_c = False
                up_c = False
                dig_c = False
                sym_c = False

    round = random.randint(0,3) # number of uppercase characters to add
    i = 0
    if round > 0 and up_c is False:
        up_c = True
    while i < round:
        random_up = random.choice(string.ascii_uppercase)
        password += random_up
        i += 1
        if len(password) == pass_l:
            if low_c and up_c and dig_c and sym_c: # checks if password contains all the requisites
                pop_up_show(password)
                exit()
            else:
                password = '' # password does not contain at least one requisite and is emptied
                low_c = False
                up_c = False
                dig_c = False
                sym_c = False

    round = random.randint(0,3) # number of digits to add
    i = 0
    if round > 0 and dig_c is False:
        dig_c = True
    while i < round:
        random_int = random.randint(0,9)
        password += str(random_int)
        i += 1
        if len(password) == pass_l:
            if low_c and up_c and dig_c and sym_c:
                pop_up_show(password)
                exit()
            else:
                password = ''
                low_c = False
                up_c = False
                dig_c = False
                sym_c = False

    round = random.randint(0,3) # number of special characters to add
    i = 0
    if round > 0 and sym_c is False:
        sym_c = True
    while i < round:
        random_sp = random.choice(string.punctuation)
        password += random_sp
        i += 1
        if len(password) == pass_l:
            if low_c and up_c and dig_c and sym_c:
                pop_up_show(password)
                exit()
            else:
                password = ''
                low_c = False
                up_c = False
                dig_c = False
                sym_c = False
