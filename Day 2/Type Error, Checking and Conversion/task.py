#len(12345) - it does't like working with int.
#we gonna get TypeError.

#for not getting a error.
len("Hello")

#How would we know a datatype of any data?

#Cheacking DataType
print(type("Hello")) #type function to know datatype.
print(type(123))
print(type(3.14))
print(type(True))

#Type Casting or Type Coversion.
print("123" + "456") #this will treat as string.
print(int("123") + int("456"))
#But sometimes you can't convert things into different DataType.
#print(int("abc") + int("456"))
#this'll give a ValueError

#Task - make this code to give TypeError.
#print("Number of letters in your name: " + len(input("Enter your name")))

#Solution
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))
