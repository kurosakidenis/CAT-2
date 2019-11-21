"""
Write a Python function to check whether a number is divisible by another number.
Accept two integers values from the user.

"""

first_num = int(input('Enter the first Number:' ))
second_num = int(input('Enter the Second Number:' ))

if first_num % second_num == 0 and second_num % first_num:
    print('The two number you entered ARE DIVISIBLE to each other')
else:
    print('The two number you entered ARE NOT DIVISIBLE to each other')