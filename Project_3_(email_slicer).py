#Ask user for email

email=input("What is your email address :")

#slice out user name

user_name=email[:email.index("@")]

#slice domain name

domain_name=email[email.index("@")+1:]

#Format message

Output="Your username is {} and your domain name is {}".format(user_name,domain_name)

#Display output on screen

print(Output)
