#Ask user for name

print("Enter your name :")

user_name=input()

#Ask user for age

print("Enter user age :")

user_age=input()

#Ask user for user's place

print("Enter user's place :")

user_place=input()

#Ask user what they enjoy

print("What do you love ?")

user_love=input()

#Creating output text

String="Your name is {}.Your age is {}.You live in {} and you love {}."

output=String.format(user_name,user_age,user_place,user_love)

#Print output screen

print(output)
