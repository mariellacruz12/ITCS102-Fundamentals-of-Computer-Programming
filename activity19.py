from getpass import getpass
islogin=False
loginAttempts=0

username="admin"
password="dikonakaya"

while islogin == False:
    uname = input("Enter your username ---> ")
    pword = getpass("Enter your password ---> ")

    if uname == username and pword == password:
        print("Login successful!")
        print("Total Login Attempts: ", loginAttempts)
        islogin = True
    else:
        print("Login failed! Please try again.")
        loginAttempts += 1
        islogin = False