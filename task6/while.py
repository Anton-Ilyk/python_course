#Program which asking user to input the numbers,
#if user input number will be "-1", program will show the sum of the previous numbers(except -1)
user_num = 0 
num_sum = 0
tries = 0

while user_num != -1:
    user_num = input("Please, enter a number: ")
    #Check if user input is exists number;create sum and average number; showing result
    try:                                         
        user_num = int(user_num)
        if user_num != -1:
            num_sum += user_num
            tries += 1
        else:
            sum_avg = num_sum / tries
            print(f"The average of the entered numbers: {sum_avg}")
    except:
        print("\nThis is not a number! Input correct number!\n")