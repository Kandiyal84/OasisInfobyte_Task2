import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()><?}{][/*-+.}"

while 1: 
    password_length = int(input("what long do you want your passwrod to be? : "))
    password_count = int(input("how many passwords do you want? : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_length):
            password_char = random.choice(characters)
            password = password + password_char
        print("Here's your password : ", password)
