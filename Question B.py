"""
Write a python program to calculate the compound interest.
Use the formula A= P(1 + R/100)^t.

"""
import math
rate = int(input('What was the interest rate: '))
principal = float(input('Please enter the Initial Principal Balance: '))
time = int(input('Please enter the time elapsed(years)'))

k = 1 + rate/100
amount = principal * k
final_amount = pow(amount, time)
print(amount)
print('The total Amount is: ',final_amount)



