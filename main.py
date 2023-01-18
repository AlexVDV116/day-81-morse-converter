from art import logo
from playsound import playsound
import time


# Plays the corresponding morse code audio file for each symbol in the morse_code
def play_sound(morse_code):
    for symbol in morse_code:
        if symbol == ".":
            playsound("DIT.wav")
        elif symbol == "-":
            playsound("DAH.wav")
        elif symbol == " ":
            time.sleep(3)
        else:
            time.sleep(1)


morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                   'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                   'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                   'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}

# Generates a list of accepted keys in the morse_code_dict
key_list = [key for key in morse_code_dict]
keys = ""
for key in key_list:
    keys += key + ", "

print(logo)
app_on = True
while app_on:
    user_input = input("Text input: ").lower()
    # Conditional list comprehension to checks if a character in the user input does not exist in the morse_code_dict
    # and adds that character to the problems list
    problems = [char for char in user_input if char not in morse_code_dict]
    if problems:
        problem_characters = ""
        for char in problems:
            problem_characters += char + ", "
        print(f"Character error on: {problem_characters}")
        print(f"List of accepted characters:\n{keys}")
    else:
        # List comprehension that adds the corresponding morse code value to each char in user input
        output_list = [morse_code_dict[char] for char in user_input]
        # Use the join method to join all items in the output_list with a space as the seperator
        result = ' '.join(output_list)
        print(f"Morse code output:\n{result} ")

        play_sound_input = input("Play morse code audio?  (Y/N):").upper()
        if play_sound_input == "Y":
            print("Playing morse code audio...")
            play_sound(result)

        encode_again = input("Encode more text? (Y/N):").upper()
        if encode_again == "N":
            print("Terminating program.")
            app_on = False
