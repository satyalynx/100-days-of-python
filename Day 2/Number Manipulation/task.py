bmi = 84 / 1.65 ** 2 #it's not a ideal way actually.
print(bmi)

print(int(bmi)) #that's flooring.

#we want rounding - which rounds up to the nearest whole number.
print(round(bmi))
print(round(bmi, 2)) #can also put the no. of digits, wants to round it to.

#Assignment Operator - to accumulate the results of calculation.
#Example -
score = 0
#user scores of point
score += 1
print(score)

#f-strings
print("Your score is " + str(score))  #not handy

#Example(precise)
score = 0
height = 1.0
is_winning = True

#f - in front of a string we type f with quote.

#better to write like
print(f"Your score is = {score}, Your height is {height}. You are winning is {is_winning}")
#All of this different datatype are correct using 'f' string.

