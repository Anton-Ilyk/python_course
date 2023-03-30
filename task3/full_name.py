full_name = str(input("Please input your full name: "))

check_len = len(full_name)

if check_len == 0:
    print("You haven’t entered anything. Please enter your full name.")
elif check_len < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif check_len > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")