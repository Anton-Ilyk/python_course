#This programme works as a finance calculator or a repayment calculator, depends what do you need of it
import math


#Explaining functions of the programme; choosing type of the calculator; checking and confirming that user choose right type of calculator
calc_type = ""
while calc_type == "":
    user_input = str(input("""investment - to calculate the amount of interest you`ll earn on your investment
bond       - to calculate the amount of interest you`ll have to pay on a home loan\n
Enter either 'investment' or 'bond' from the menu above to proceed: \n"""))

    if user_input == "BOND" or user_input == "bond" or user_input == "Bond":
        calc_type = "bond"
    elif user_input == "investment" or user_input == "Investment" or user_input == "INVESTMENT":
        calc_type = "invest"
    else:
        print("\nChosen type of the calculator not supported by this programme!\n")

#Calculating interest for each type of deposit calculator
if calc_type == "invest":
    #Collecting users data
    users_deposit = int(input("\nWhat amount of the money that you would like to deposit(£): "))
    int_rate = int(input("Please, input the yearly interest rate(%): "))/100                               #Calculating theinterest rate which will be ready for using in calculations
    inv_years = int(input("How many years you would like to hold this deposit: "))

    #Checking for the right type of deposit(for not to start everything from the start, if yuser made mistake here)
    interest = str(input("Would you prefer \"simple\" or \"compound\" type of deposit: "))
    while not(interest == "Simple" or interest == "simple" or interest == "SIMPLE" or interest == "COMPOUND" or interest == "Compound" or interest == "compound"):
        interest = str(input("\nPlease, enter right type of deposit!\nWould you prefer \"simple\" or \"compound\" type of deposit: "))
        
    #Calculating amount of money for the simple deposit
    if interest == "Simple" or interest == "simple" or interest == "SIMPLE":
        total_amount = round(users_deposit * (1 + int_rate * inv_years), 2)
        print(f"\nYour total amount of the money on your deposit account after {inv_years} years will be £{total_amount}.\n")

    #Calculating amount of money for the compound deposit
    if interest == "compound" or interest == "Compound" or interest == "COMPOUND":
        total_amount = round(users_deposit * math.pow((1 + int_rate), inv_years), 2)
        print(f"\nYour total amount of the money on your deposit account after {inv_years} years will be £{total_amount}.\n") 

#Calculating the amount you need to pay monthly on a home loan
if calc_type == "bond":
    #Collecting users data
    house_value = int(input("\nWhat is the value of the house which you want to buy(£): "))
    loan_rate = (int(input("Please, input the yearly interest rate(%): "))/100)/12                           #Calculating the monthly interest rate which will be ready for using in calculations
    repay_term = int(input("How many months you plan to repay your loan: "))
    
    #Calculating and showing monthly payment
    repayment = round((loan_rate * house_value) / (1 - math.pow((1 + loan_rate),(-repay_term))), 2)
    print(f"\nYour monthly payment will be £{repayment} for the next {repay_term} months.\n")