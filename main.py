# import random
#
# lottery = random.randint(0, 100)
# if 50 < lottery < 80:
#     print('You win bunny!', f'you get {lottery}')
# elif 80 <= lottery:
#     print('You get jackpot', f'you get {lottery}')
# else:
#     print('Lost', f'{lottery} is to small result')
#
# # Write a program that reads in the user's salary and divides the number by 12 months. The monthly salary should be
# # output to the console with 0 decimal places rounded up.
#
# # For example, if the user enters 60000 the program should display 5000
#
# # The file should be name lab.py and a file is included you can start with
#
# annualsalary = float(input(""))
# monthsalary = int(round(float(annualsalary / 12.0)))
# print(monthsalary)
#
# # Write a program that reads in a whole number and divides it by 3 and displays the result with three decimal places
# # if they exist(rounded up).
# #
# #     For example, if the user enters 2 the program should display 0.667
# #
# #     For example, if the user enters 9999 the program should display 3,333.0
# #
# # The file should be name lab.py and a file is included you can start with
#
# readnumber = int(input(''))
# number = round(readnumber / 3, 3)
# print(number)
#
# # Write a program that reads in a number and prints the either Small, Medium or Large depending on if the number is
# # bellow 100 or above 200.
# #
# #     For example, if the user enters 150 the program should display “Medium”
# #
# #     Another example, is if the user enters 50 the program should display “Small”
# #
# # The file should be name lab.py and a file is included you can start with
#
# readnumber = int(input())
# if readnumber < 100:
#     print('Small')
# elif readnumber <= 200:
#     print('Medium')
# else:
#     print('Large')

# Write a program that reads in a number and prints the sum of all values from 1 up to the number.
#
#     For example, if the user enters 5 the program should display 15.  15 is (1+2+3+4+5)
#
# The file should be name lab.py and a file is included you can start with.

rnumber = int(input())
sum = 0
for num in range(1, rnumber+1):
    sum = sum + num

print(sum)


# Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered.
#
# For example, if the user enters 5 10 15 -1 the program should display 30 (Each number will be separated by a
# carriage return).  30 is (5+10+15)
#
# The file should be name lab.py and a file is included you can start with.

sum = 0
while True:
    rnum = int(input())
    if rnum != -1:
        sum = sum + rnum
    else:
        break
print(sum)

