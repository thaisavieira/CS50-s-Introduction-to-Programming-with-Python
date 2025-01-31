#prompts the user for input and then outputs that same input, replacing each space with ...

def main():
    user_input = input(str("Start your lecture: "))
    playback(user_input)

def playback(user_input):
    converting_to_slow_speed = user_input.replace(" ", "...")
    print(converting_to_slow_speed )


main()
