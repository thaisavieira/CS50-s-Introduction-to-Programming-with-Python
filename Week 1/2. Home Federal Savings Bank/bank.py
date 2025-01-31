#  a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    user_input = str(input('Greeting: ')).lower().strip()
    greeting(user_input)

def greeting(user_input):
    if user_input[0:5] == 'hello':
        print('$0')
    elif user_input[0] == 'h':
        print('$20')
    else:
        print('$100')
main()

