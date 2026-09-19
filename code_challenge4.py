#LOAN APPLICATION SYSTEM

print("==========Welcome to the Loan Application System!==========")
print("==========Please log in to continue.==========")

correct_user="ifeelsoBSITrn"
correct_pass="akalakotypetypelang"

username=input("Enter your username ---> ")
password=input("Enter your password ---> ")

if username==correct_user and password==correct_pass:
    print("==========Log in successfull! Access Granted!==========")
else:
    print("==========Access Denied! Invalid username or password.==========")
    exit()

print("==========Please provide the following information to determine your eligibility for a loan.==========")

name=input("Enter your name ---> ")
job_title=input("What is your job title? ---> ")
collateral=input("What are your collaterals? ---> ")
value_of_collateral=eval(input("What is the value of your collateral? ---> "))
amount_of_loan=eval(input("How much is your loan amount? ---> "))

if value_of_collateral <= 30000:
    print("==========Sorry, your collateral value is too low to secure a loan.==========")
    exit()
else:
    print("==========Your loan amount is approved with a base interest rate of 5%.=========")
    print("Provide your credit score history and annual income to determine your eligibility for a loan.")

age=int(input("Enter your age ---> "))
is_employed = bool(input("Are you currently employed? ---> "))
credit_score = eval(input("Credit Score History ---> "))
annual_income = eval(input("How much is your annual income---> "))
has_collateral = bool(input("Do you have any collateral? ---> "))

if age < 21 or age > 65 == True:
    print("==========Sorry, you are not eligible for a loan due to age restrictions.==========")
    exit()

    if credit_score >= 750:
        base_interest_rate_tier1 = 5.0
        if annual_income >= 100000:
            interest_rate_tier1 = base_interest_rate_tier1 - 0.5
        else:
            interest_rate_tier1 = base_interest_rate_tier1

        print("==========You are eligible for a loan with an interest rate of", interest_rate_tier1, "%.==========")

    elif credit_score >= 600:
        base_interest_rate_tier2 = 8.0
        if annual_income < 40000:
            interest_rate_tier2 = base_interest_rate_tier2 + 1.5
        elif has_collateral == True:
            interest_rate_tier2 = base_interest_rate_tier2 - 1.0
        else:
            interest_rate_tier2 = base_interest_rate_tier2

        print("==========You are eligible for a loan with an interest rate of", interest_rate_tier2, "%.==========")

    elif credit_score < 600:
        print("==========You are not eligible for a loan due to low credit score.==========")

else:
    print("==========REJECTED! You must be at least 21 years old and currently employed to apply for a loan.==========")
