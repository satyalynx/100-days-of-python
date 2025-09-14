#Modulo Operator - %

#Operator - An Operator is a symbol in programming that has a function.
"""Modulo Operator - is a binary operator, and give us the reminder
                     after the division between 2 numbers.
                     10%5=2 - no reminder(completely divisible)."""

#Check Odd or Even
number_to_check = int(input("What is a number you want to check? "))

print(number_to_check % 2)
#this will give you odd number if we give odd number.

#to check Even or Odd
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")