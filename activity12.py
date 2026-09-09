#multiple if and elif conditions

name = input("Please input your name --->")
age = int(input("Please input your age --->"))

if age >= 0 and age <= 5 :
            print("That age is considered as INFANT")

elif age >= 6 and age <= 12 :
            print("That age is considered as a KID")

elif age >= 13 and age <= 15 :
            print("That age is considered as a PRE TEEN")

elif age >= 16 and age <= 19 :
            print("That age is considered as a TEENAGER")

elif age >= 20 and age <= 21 :
            print("That age is considered as a EARLY ADULTHOOD")

elif age >= 22 and age <= 25 :
            print("AGE INVALID")
