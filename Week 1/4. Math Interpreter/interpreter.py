# a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein: x is an integer,y is +, -, *, or /,and,z is an integer


# get user input
expression = input('Expression: ')
#convert this into variables
x, y, z = expression.split(" ")
#change type of variables x and z to float
new_x = float(x)
new_z = float(z)
#calculate the result
if y == '+':
    result = new_x + new_z
elif y =='-':
    result = new_x - new_z
elif y == '*':
    result = new_x * new_z
elif y == "/":
    result = new_x / new_z
print(result)
