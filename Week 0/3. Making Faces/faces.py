# implement a function that accepts a str and returns that same input with any :) converted to 🙂 and any :( converted to 🙁

def main():
    user_input = input(str("How are you feeling today? "))
    convert(user_input)

def convert(user_input):
    converting_to_emojis = user_input.replace(":)","🙂").replace(":(","🙁")
    print(converting_to_emojis)

main()
