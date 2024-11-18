#!/usr/bin/python
import os

# File to store user data
USER_FILE = 'users.txt'

# Function to load users from the file
def load_users():
    users = []
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            for line in file:
                username, pin, balance = line.strip().split(',')
                users.append({'username': username, 'pin': pin, 'balance': int(balance)})
    return users

# Function to save users to the file
def save_users(users):
    with open(USER_FILE, 'w') as file:
        for user in users:
            file.write(f"{user['username']},{user['pin']},{user['balance']}\n")

# Load users from the file
users = load_users()
if not users:
    # Initialize with default data if file is empty
    users = [
        {'username': 'user1', 'pin': '1111', 'balance': 1000},
        {'username': 'user2', 'pin': '2222', 'balance': 2000},
        {'username': 'user3', 'pin': '3333', 'balance': 3000},
    ]
    save_users(users)

# User login
while True:
    username = input('\nENTER USER NAME: ').lower()
    user = next((u for u in users if u['username'] == username), None)
    if user:
        break
    else:
        print('INVALID USERNAME')

# Verify PIN
attempts = 0
while attempts < 3:
    pin = input('PLEASE ENTER PIN: ')
    if pin == user['pin']:
        break
    else:
        attempts += 1
        print('INVALID PIN')
if attempts == 3:
    print('3 UNSUCCESSFUL ATTEMPTS. EXITING.')
    exit()

print(f'LOGIN SUCCESSFUL. Welcome, {username.capitalize()}!')

# Main menu
while True:
    print("\nSELECT AN OPTION: ")
    print("Balance__(B) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q)")
    response = input("Your choice: ").lower()

    if response == 'b':
        print(f"Your balance is {user['balance']} rupees.")
    elif response == 'w':
        amount = int(input('ENTER AMOUNT TO WITHDRAW: '))
        if amount % 10 != 0:
            print('AMOUNT MUST BE A MULTIPLE OF 10.')
        elif amount > user['balance']:
            print('INSUFFICIENT BALANCE.')
        else:
            user['balance'] -= amount
            print(f"WITHDRAWAL SUCCESSFUL. NEW BALANCE: {user['balance']} rupees.")
            save_users(users)
    elif response == 'l':
        amount = int(input('ENTER AMOUNT TO LODGE: '))
        if amount % 10 != 0:
            print('AMOUNT MUST BE A MULTIPLE OF 10.')
        else:
            user['balance'] += amount
            print(f"LODGEMENT SUCCESSFUL. NEW BALANCE: {user['balance']} rupees.")
            save_users(users)
    elif response == 'p':
        new_pin = input('ENTER NEW PIN: ')
        if len(new_pin) == 4 and new_pin.isdigit() and new_pin != user['pin']:
            confirm_pin = input('CONFIRM NEW PIN: ')
            if confirm_pin == new_pin:
                user['pin'] = new_pin
                print('PIN UPDATED SUCCESSFULLY.')
                save_users(users)
            else:
                print('PIN MISMATCH. TRY AGAIN.')
        else:
            print('INVALID PIN FORMAT. MUST BE 4 DIGITS AND DIFFERENT FROM CURRENT PIN.')
    elif response == 'q':
        print('EXITING. THANK YOU!')
        break
    else:
        print('INVALID OPTION. TRY AGAIN.')
