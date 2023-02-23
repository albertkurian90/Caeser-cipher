from os import system, name

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(msg, shift_count):
    """
        Function to enrypt a given input with ceasar encryption method.

        Args:
            text (str): Message to be encoded.
            shift (int): Number of character shifts for cipher.

        Returns:
            str: Encoded message.
    """
    encrypted_text = ""
    for character in msg:
        if character not in alphabet:
            encrypted_char = character
        else:
            position = alphabet.index(character)
            encrypted_char_position = position + shift_count
            while encrypted_char_position > 25:
                encrypted_char_position -= 26
            encrypted_char = alphabet[encrypted_char_position]
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(msg, shift_count):
    """
        Function to decrypt a given input with ceasar decryption method.

        Args:
            text (str): Message to be decoded.
            shift (int): Number of character shifts for cipher.

        Returns:
            str: Decoded message.
    """
    decrypted_text = ""
    for character in msg:
        position = alphabet.index(character)
        decrypted_char_position = position - shift_count
        while decrypted_char_position > 25:
            decrypted_char_position -= 26
        decrypted_char = alphabet[decrypted_char_position]
        decrypted_text += decrypted_char
    return decrypted_text


def clear_terminal():
    """
        Clear terminal
    """
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux
    else:
        system('clear')
