len("Hello") #len fn used to get the no. of characters in a string.

print(len("Hello"))
#let's say we put in a number instead, find no. of digits.
#print(len(1234)) - it'll crash

#What's all of this about?
#to understand - we have to know "datatypes"

#some of the most basic datatypes: String, float, Integer, boolean
"Hello" #just string of character.right!

#we can actually pull out each character individually.
print("Hello"[0]) #you'll get "H"
#so, programmers always count with zero.
#so, the first of anything is zero.

#Subscripting - this is the name of above method
#Note: You can also use a '-ve' number. this holds the last character.

#String
print("123")
print("123" + "456") #concatenation
#anything inside quote is a string.

#Integer
print(123 + 456)
#large integer
print(123,456,789) #in python, replace these comas into '_'.
print(123_456_789)#interpreted as - 123456789

#Float
print(3.12159)
""" If you think of a decimal point is being able to float around the number, because it could occur at any point, then you've got yourself a floating point number."""

#Boolean
print(True)
print(False)
""" Always begin with capital 'T' and 'F'. And no quotation marks around them."""
