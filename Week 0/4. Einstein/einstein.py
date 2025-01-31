#prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.

def main():
    m = int(input("Type a mass value in kilograms: "))
    einstein(m)

def einstein(m):
    c = 300000000**2
    e = m*c
    print('e =', e)

main()
