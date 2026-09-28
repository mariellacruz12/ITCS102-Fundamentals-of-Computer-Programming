#inputs

owner_age=int(input("Enter Your Age"))
monthly_rev=float(input("Enter your monthly revenue"))
credit_score=int(input("Enter Your Credit Score"))
yrs_b=float(input("Enter your years in business"))
has_def=bool(input("Do you have history of bankcruptcy?"))
coll_name=str(input("Enter your collaterals"))
coll_val=float(input("Enter your collateral value"))

max_limit=0.0
base_fee=0.0
if owner_age >= 21 and yrs_b >= 2 and has_def == False:
    print("Baseline Requirements Passed")
    if coll_val >= 720: #tier1
        max_limit=monthly_rev*3
        print("max loan for high credit score is ", max_limit)
        print("High Credit")
        if monthly_rev >= 50000:
            base_fee=max_limit*0.015
            print("base fee rate is ", base_fee)
        else:
            base_fee=max_limit*0.025
            print("base fee rate is ", base_fee)

        if coll_val >= max_limit:
            print("Collateral",coll_name,"---ACCEPTED")
        else:
            print("Collateral not accepted")
    else:
        print("Not Tier 1")
else:
    print("Passed")

