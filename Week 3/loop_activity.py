# Activity 1- create a look that prints "hello world" 13 times. Then convert this into a while look that does the same job.

for i in range(13):
    print("Hello World")


# Activity 2- use a nested for loop to write a programme which prints out multiplication tables from 1 to 12

for i in range(1,13):
    for j in range(1,13):
        print(i * j)
        print("\n")
# would be better in table format- how do you create this? How to line break after each multiplication?

# Activity 3

password = input("Please enter your password:   ")
password_attempt = 3 

while password == "codenation1234":
    print("Welcome to your account")
    password = input("Please enter your password:   ")
else:
    print("Your password is incorrect, please try again")

