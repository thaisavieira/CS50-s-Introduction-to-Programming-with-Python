# a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')

def convert(time):
    #get hour and minute
    hours, minutes = time.split(":")
    #convert time into float mumber
    new_minutes = float(minutes)/60
    #return the result to main function
    return (float(hours) + new_minutes)

if __name__ == "__main__":
    main()
