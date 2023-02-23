from time import sleep
from art import tprint
import util as u

FLAG = True
tprint("CEASAR\nCIPHER")
while FLAG:
    direction = input(
        "Type 'e' to encrypt, type 'd' to decrypt, type 'q' to quit:\n")
    if direction != "q":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # Allowing all postive integers to be passed as shift number
        if shift > 26:
            shift = shift % 26

        if direction == "e":
            encoded_text = u.encrypt(text, shift)
            
            print(f"Encoded message is:\n{encoded_text}\n")
            sleep(1)
        elif direction == "d":
            print(f"Decoded message is:\n{u.decrypt(text, shift)}\n")
            sleep(1)
        else:
            print("Sorry invalid input\n")

        clear_flag = input(
            "Would you like a clean terminal?\n Enter 'y' for Yes, type any for No\n")
        if clear_flag == "y":
            u.clear_terminal()
    else:
        FLAG = False
