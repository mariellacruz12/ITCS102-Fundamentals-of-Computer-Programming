#import demo
import getpass

username = "oopsoops"
password = "ayoko_na"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")

if u == username or p == password :
        print("username and password correct")

else:
        print("access denied")