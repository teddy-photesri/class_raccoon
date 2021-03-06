'''
Lab 8: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered

conditionals, comparisons
arithmetic


Version 1

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.
'''

#User needs to choose how many pennies
pennies = int(input("How many pennies?\n"))

quarters = pennies // 25 #because quarters are 25 with no remainder

pennies = pennies % 25 #because we need to use the remainder after quarters are calculated to get the amount in order to calculate the next biggest value, in order to get the fewest amount of coins

dimes = pennies // 10

pennies = pennies % 10

nickles = pennies // 5

pennies = pennies % 5

#calculation printed. shows the user
print(f"\n\n\n\n\n\nThis the fewest amount of coins you can have w dat many cents. hehe\n\nquarters: {quarters}\ndimes: {dimes}\nnickles: {nickles}\npennies: {pennies}\n\nsee ya!\n\n")
