#The programm will print stars from the output_star variable; each time programm will print one start more than the previous time

#Extra check to follow task(at least 5 stars); extra check on correct type of data
output_star = input("Please, input amount of the stars(minimum 5): ")
while type(output_star) != int:
    try:                                         
        output_star = int(output_star)
        if output_star < 5:
            output_star = input("You need to input more than 5 STARS: ")    
    except:
        output_star = input("Please, input exists number: ")

#Loop FOR for printing STARS in the TERMINAL
for i in range(1, output_star + 1):
    star_list = ""
    for f in range(i):
        star_list = star_list + ("*")
    print(star_list)    



#!BONUS FROM DEVELOPER! Extra variant of completing this task is below
# You can change amount of stars in output_star and everything will work! =)

"""

output_star = "*****"

for i in range(1, (len(output_star) + 1)):
    print(output_star[0:i])
    
"""