# prompts the user for input and then outputs that same input in lowercase.

def main():
    user_input = input(str("What did you say? "))
    indoor(user_input)

def indoor(user_input):
    convert_to_lowercase = user_input.lower()
    print(f"I'm not deaf... Just speak normally, please: {convert_to_lowercase}")

main()
