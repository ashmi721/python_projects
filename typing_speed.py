# wap to create a self typing practice app
from time import time
import random

def find_errors(original, user_input):
    errors = 0
    for i in range(len(original)):
        try:
            if i >= len(user_input):
                errors += 1
            elif original[i] != user_input[i]:
                errors += 1
        except:        
            errors += abs(len(original) - len(user_input))  # account for extra characters in user input
        return errors

def calculate_speed(start_time, end_time, user_input):
    time_elapsed = end_time - start_time
    speed = len(user_input) / time_elapsed
    return round(speed, 2)

if __name__ == '__main__':
    while True:
        choice = input('Ready to test? (yes/no): ')
        if choice == 'yes':
            texts = [
                "It is the only domesticated species in the family.",
                "It differs from the wild members of the family.",
                "A programming language is an artificial language",
                "that can be used to control the behavior of a machine, particularly a computer.",
                "The company owns and operates Facebook, Instagram, Threads, and WhatsApp, among other products and services.",
                "Google LLC is an American multinational technology company focusing on artificial intelligence, online advertising."
            ]
            text = random.choice(texts)
            print("****** Typing Speed ******")
            print(text)
            print()

            start_time = time()
            user_input = input("Enter: ")
            end_time = time()

            speed = calculate_speed(start_time, end_time, user_input)
            errors = find_errors(text, user_input)

            print('Speed: {} w/s'.format(speed))
            print('Errors: {}'.format(errors))
        elif choice == 'no':
            print("Thank you for using our program!")
            break
        else:
            print("Wrong input. Please enter 'yes' or 'no'.")
