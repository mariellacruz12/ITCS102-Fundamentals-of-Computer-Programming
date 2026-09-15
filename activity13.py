age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you currently employed? ---> "))
credit_score = eval(input("Credit Score History ---> "))
annual_income = eval(input("How much is your annual income---> "))
has_collateral = bool(input("Do you have any collateral? ---> "))


if age >= 21 and is_employed == True:
    if credit_score >= 750:
        base_interest_rate_tier1 = 5.0
        if annual_income >= 100000:
            interest_rate_tier1 = base_interest_rate_tier1 - 0.5
        else:
            interest_rate_tier1 = base_interest_rate_tier1

        print("You are eligible for a loan with an interest rate of", interest_rate_tier1, "%.")

    elif credit_score >= 600:
        base_interest_rate_tier2 = 8.0
        if annual_income < 40000:
            interest_rate_tier2 = base_interest_rate_tier2 + 1.5
        elif has_collateral == True:
            interest_rate_tier2 = base_interest_rate_tier2 - 1.0
        else:
            interest_rate_tier2 = base_interest_rate_tier2

        print("You are eligible for a loan with an interest rate of", interest_rate_tier2, "%.")

    elif credit_score < 600:
        print("You are not eligible for a loan due to low credit score.")

else:
    print("REJECTED! You must be at least 21 years old and currently employed to apply for a loan.")
