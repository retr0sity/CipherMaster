"""
 ________  ___      ___ _______   ___   _________  ________  ________  ___  ___  ________  _________  ________  ________  ________      
|\   ____\|\  \    /  /|\  ___ \ |\  \ |\___   ___\\   __  \|\   ____\|\  \|\  \|\   __  \|\___   ___\\_____  \|\   __  \|\   ____\     
\ \  \___|\ \  \  /  / | \   __/|\ \  \\|___ \  \_\ \  \|\  \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_|\|___/  /\ \  \|\  \ \  \___|_    
 \ \_____  \ \  \/  / / \ \  \_|/_\ \  \    \ \  \ \ \  \\\  \ \_____  \ \   __  \ \  \\\  \   \ \  \     /  / /\ \   __  \ \_____  \   
  \|____|\  \ \    / /   \ \  \_|\ \ \  \____\ \  \ \ \  \\\  \|____|\  \ \  \ \  \ \  \\\  \   \ \  \   /  /_/__\ \  \ \  \|____|\  \  
    ____\_\  \ \__/ /     \ \_______\ \_______\ \__\ \ \_______\____\_\  \ \__\ \__\ \_______\   \ \__\ |\________\ \__\ \__\____\_\  \ 
   |\_________\|__|/       \|_______|\|_______|\|__|  \|_______|\_________\|__|\|__|\|_______|    \|__|  \|_______|\|__|\|__|\_________\
   \|_________|                                                \|_________|                                                 \|_________|                                                                                                                                       
"""

import math

# Caesar Cipher
def caesar_cipher(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def caesar_decipher(ciphertext, key):
    return caesar_cipher(ciphertext, -key)


# Vigenere Cipher
def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_len = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(
                    (ord(char) - ord('A') + ord(key[i % key_len].upper()) - ord('A')) % 26 + ord('A')
                )
            else:
                encrypted_char = chr(
                    (ord(char) - ord('a') + ord(key[i % key_len].lower()) - ord('a')) % 26 + ord('a')
                )
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def vigenere_decipher(ciphertext, key):
    decipher_key = ''.join(chr((26 - (ord(k.upper()) - ord('A'))) % 26 + ord('A')) for k in key)
    return vigenere_cipher(ciphertext, decipher_key)


# Affine Cipher
def affine_cipher(plaintext, a, b):
    
    
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                encrypted_char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def affine_decipher(ciphertext, a, b):
    inverse_a = None
    for i in range(26):
        if (a * i) % 26 == 1:
            inverse_a = i
            break
    if inverse_a is None:
        return "Invalid key: 'a' has no inverse."
    decipher_key = (-inverse_a * b) % 26
    return affine_cipher(ciphertext, inverse_a, decipher_key)


# Hill Cipher
# Function to calculate the modulo inverse of a number
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Function to encrypt plaintext using Hill Cipher
def hill_cipher(plaintext, key):
    size = len(key)
    ciphertext = ""
    for i in range(0, len(plaintext), size):
        # Convert a block of plaintext letters to their respective numerical values
        block = [ord(ch) - ord('A') for ch in plaintext[i:i+size]]
        # Apply the key matrix multiplication
        encrypted_block = []
        for j in range(size):
            value = 0
            for k in range(size):
                value += key[j][k] * block[k]
            encrypted_block.append(value % 26)
        # Convert the numerical values back to letters
        encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_block)
        ciphertext += encrypted_text
    return ciphertext

# Function to decrypt ciphertext using Hill Cipher
def hill_decipher(ciphertext, key):
    size = len(key)
    decrypted_text = ""
    # Calculate the determinant and modulo inverse of the determinant
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det %= 26
    det_inv = mod_inverse(det, 26)
    if det_inv == -1:
        print("Invalid key! The determinant has no modulo inverse.")
        return decrypted_text
    # Calculate the adjugate matrix of the key
    adjugate_key = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    for i in range(size):
        for j in range(size):
            adjugate_key[i][j] *= det_inv
            adjugate_key[i][j] %= 26
    for i in range(0, len(ciphertext), size):
        # Convert a block of ciphertext letters to their respective numerical values
        block = [ord(ch) - ord('A') for ch in ciphertext[i:i+size]]
        # Apply the adjugate key matrix multiplication
        decrypted_block = []
        for j in range(size):
            value = 0
            for k in range(size):
                value += adjugate_key[j][k] * block[k]
            decrypted_block.append(value % 26)
        # Convert the numerical values back to letters
        decrypted_text += ''.join(chr(num + ord('A')) for num in decrypted_block)
    return decrypted_text


# Substitution Cipher
def substitution_cipher(plaintext, substitution_key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isalpha():
            # Encrypt only alphabetical characters
                char = char.upper()
                ciphertext += substitution_key.get(char, char)
        else:
            ciphertext += char
    return ciphertext


def substitution_decipher(ciphertext, substitution_key):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            # Decrypt only alphabetical characters
            char = char.upper()
            for k, v in substitution_key.items():
                if v == char:
                    decrypted_message += k
                    break
        else:
            decrypted_message += char
    return decrypted_message


# One-Time Pad (OTP)
def one_time_pad(plaintext, otp_key):
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(
                    (ord(char) - ord('A') + ord(otp_key[i % len(otp_key)].upper()) - ord('A')) % 26 + ord('A')
                )
            else:
                encrypted_char = chr(
                    (ord(char) - ord('a') + ord(otp_key[i % len(otp_key)].lower()) - ord('a')) % 26 + ord('a')
                )
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def one_time_pad_decipher(ciphertext, otp_key):
    decipher_key = ''.join(chr((26 - (ord(k.upper()) - ord('A'))) % 26 + ord('A')) for k in otp_key)
    return one_time_pad(ciphertext, decipher_key)





def menu(algorithm, plaintext):
        if algorithm == 1:
            key = input("Enter the key for Caesar Cipher: ")
            while not key.isdigit():
                error_menu(plaintext, algorithm)
            key = int(key)
            ciphertext = caesar_cipher(plaintext, key)
            print("Ciphertext:", ciphertext)
            choice = input("Do you want to decipher the ciphertext? (y/n): ")
            if choice.lower() == "y":
                decrypted_plaintext = caesar_decipher(ciphertext, key)
                print("Deciphered plaintext:", decrypted_plaintext)
                exit()
            else:
                exit()

        elif algorithm == 2:
            key = input("Enter the key for Vigenere Cipher: ")
            while not key.isalpha():
                error_menu(plaintext, algorithm)
            ciphertext = vigenere_cipher(plaintext, key)
            print("Ciphertext:", ciphertext)
            choice = input("Do you want to decipher the ciphertext? (y/n): ")
            if choice.lower() == "y":
                decrypted_plaintext = vigenere_decipher(ciphertext, key)
                print("Deciphered plaintext:", decrypted_plaintext)
                exit()
            else:
                exit()

        elif algorithm == 3:
            a = input("Enter the multiplicative key for Affine Cipher: ")
            while (not a.isdigit()):
                print("\nError: No numbers were given\n")
                error_menu(plaintext, algorithm)
            a = int(a)
            b = input("Enter the additive key for Affine Cipher: ")
            while not b.isdigit():
                print("\nError: No numbers were given\n")
                error_menu(plaintext, algorithm)
            b = int(b)
            while (not (isinstance(a, int) and isinstance(b, int))) or (a == 0 or b == 0) or (math.gcd(a, 26) != 1):
                print("\nWrong keys\n")
                error_menu(plaintext, algorithm)
            ciphertext = affine_cipher(plaintext, a, b)
            print("Ciphertext:", ciphertext)
            choice = input("Do you want to decipher the ciphertext? (y/n): ")
            if choice.lower() == "y":
                decrypted_plaintext = affine_decipher(ciphertext, a, b)
                print("Deciphered plaintext:", decrypted_plaintext)
                exit()
            else:
                exit()


        elif algorithm == 4:
            key = []
            key_size = input("Enter the size of the key matrix for Hill Cipher: ")
            while not key_size.isdigit():
                print("\nError: No numbers were given\n")
                error_menu(plaintext, algorithm)
            key_size = int(key_size)
            for i in range(key_size):
                row = []
                for j in range(key_size):
                    element = input(f"Enter element at position ({i + 1}, {j + 1}): ")
                    while not element.isdigit():
                        print("\nError: No numbers were given\n")
                        error_menu(plaintext, algorithm)
                    element = int(element)
                    row.append(element)
                key.append(row)
            ciphertext = hill_cipher(plaintext, key)
            print("Ciphertext:", ciphertext)
            choice = input("Do you want to decipher the ciphertext? (y/n): ")
            if choice.lower() == "y":
                decrypted_plaintext = hill_decipher(ciphertext, key)
                print("Deciphered plaintext:", decrypted_plaintext)
                exit()
            else:
                exit()


        elif algorithm == 5:
            substitution_key = {}
            for i in range(26):
                char = chr(ord('A') + i)
                substitution = input(f"Enter substitution for {char}: ")
                while not substitution.isalpha():
                    error_menu(plaintext, algorithm)
                substitution_key[char] = substitution
            ciphertext = substitution_cipher(plaintext, substitution_key)
            print("Ciphertext:", ciphertext)
            choice = input("Do you want to decipher the ciphertext? (y/n): ")
            if choice.lower() == "y":
                decrypted_plaintext = substitution_decipher(ciphertext, substitution_key)
                print("Deciphered plaintext:", decrypted_plaintext)
                exit()
            else:
                exit()

        elif algorithm == 6:
            otp_key = input("Enter the OTP key: ")
            while not otp_key.isalpha():
                error_menu(plaintext, algorithm)
            ciphertext = one_time_pad(plaintext, otp_key)
            print("Ciphertext:", ciphertext)
            choice = input("Do you want to decipher the ciphertext? (y/n): ")
            if choice.lower() == "y":
                decrypted_plaintext = one_time_pad_decipher(ciphertext, otp_key)
                print("Deciphered plaintext:", decrypted_plaintext)
                exit()
            else:
                exit()
    

def selector(plaintext):
    choice = input("Do you want to use the same plaintext? (y/n):")
    if choice == "n":
        plaintext = input("Enter the plaintext: ")
    algorithm = input(
        "Choose an algorithm (1-6):\n1. Caesar Cipher\n2. Vigenere Cipher\n3. Affine Cipher\n4. Hill Cipher\n5. Substitution Cipher\n6. One-Time Pad\n")
    algorithm = int(algorithm)

    while algorithm not in [1, 2, 3, 4, 5, 6]:
        print("Invalid algorithm choice. Please try again.")
        algorithm = input(
            "Choose an algorithm (1-6):\n1. Caesar Cipher\n2. Vigenere Cipher\n3. Affine Cipher\n4. Hill Cipher\n5. Substitution Cipher\n6. One-Time Pad\n")
        algorithm = int(algorithm)

    menu(algorithm, plaintext)


def main():
    plaintext = input("Enter the plaintext: ")
    algorithm = input(
        "Choose an algorithm (1-6):\n1. Caesar Cipher\n2. Vigenere Cipher\n3. Affine Cipher\n4. Hill Cipher\n5. Substitution Cipher\n6. One-Time Pad\n")
    algorithm = int(algorithm)

    while algorithm not in [1, 2, 3, 4, 5, 6]:
        print("Invalid algorithm choice. Please try again.")
        algorithm = input(
            "Choose an algorithm (1-6):\n1. Caesar Cipher\n2. Vigenere Cipher\n3. Affine Cipher\n4. Hill Cipher\n5. Substitution Cipher\n6. One-Time Pad\n")
        algorithm = int(algorithm)

    menu(algorithm, plaintext)


def error_menu(plaintext, algorithm):
    choice = input("Choose an option:\n1. Re-enter the same algorithm\n2. Use a different algorithm\n3. Exit the program\n")

    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        choice = input("Choose an option:\n1. Re-enter the same algorithm\n2. Use a different algorithm\n3. Exit the program\n")

    if choice == "1":
        menu(algorithm, plaintext)
    elif choice == "2":
        selector(plaintext)  # Pass the plaintext argument
    elif choice == "3":
        print("Exiting the program...")
        exit()

main()


