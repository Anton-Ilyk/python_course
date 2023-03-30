# The Triathlon Award calculation programme

# Explanation of correct type for the input time
print("Please, input persons best time in format that explained below.\nFor example, person time in swimming was 8 minutes and 00 seconds.\nInput this time like \"08:00\".\n\r")


swim = input("What was the best time of the person in the swimming? ")
cycle = input("What was the best time of the person in the cycling? ")
run = input("What was the best time of the person in the running? ")

# Extraction minutes and seconds from the strings
swim_min = int(swim[0:2])
swim_sec = int(swim[3:5])
cycle_min = int(cycle[0:2])
cycle_sec = int(cycle[3:5])
run_min = int(run[0:2])
run_sec = int(run[3:5])

# Converting minutes to the same numerical system as hours system, for better calculation
swim_sec = (swim_sec * 1.67)/100
cycle_sec = (cycle_sec * 1.67)/100
run_sec = (run_sec * 1.67)/100

# Calculation athletes total time for awarding system with rounding of the result
athl_time = round((swim_min + swim_sec + cycle_min + cycle_sec + run_min + run_sec), 2)

# Calculate and display athletes total time in minutes and seconds
total_min = round(((athl_time%1) * 100) / 1.67)
total_hours = int(athl_time)
print(f"\nCongratulations! You completed this competition in {total_hours} minutes and {total_min} seconds\n")

# Display type of award
if athl_time < 100:
    print("Your award is \"PROVINCIAL COLOURS\"!")
elif athl_time < 105:
    print("Your award is \"PROVINCIAL HALF COLOURS\"!")   
elif athl_time < 110:
    print("Your award is \"PROVINCIAL SCROLL\"!")  
else:
    print("Unfortunately, you don't get any reward.")          