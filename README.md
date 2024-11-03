# CipherMaster

**CipherMaster** is a command-line encryption tool designed for encrypting and decrypting text using six classical cipher algorithms. It supports a variety of ciphers, including Caesar, Vigenere, Affine, Hill, Substitution, and One-Time Pad, allowing users to experiment with and understand different encryption techniques.

## Features

- **Caesar Cipher**: A basic shift cipher that shifts each character in the plaintext by a specified key.
- **Vigenere Cipher**: Uses a keyword to shift characters, offering a more complex encryption method than Caesar.
- **Affine Cipher**: An encryption method that combines both multiplicative and additive keys for character transformations.
- **Hill Cipher**: A polygraphic cipher using matrix multiplication to encrypt character blocks.
- **Substitution Cipher**: A monoalphabetic cipher where each letter is substituted with a unique character based on a given key.
- **One-Time Pad (OTP)**: A theoretically unbreakable cipher that uses a unique key equal in length to the plaintext.

## Getting Started

### Prerequisites

Ensure that you have **Python 3.x** installed on your system. CipherMaster is a standalone Python program that doesn't require any external libraries.

### Installation

1. Clone this repository or download `CipherMaster.py` directly:

    ```bash
    git clone https://github.com/yourusername/ciphermaster.git
    cd ciphermaster
    ```

2. Run the program:

    ```bash
    python ciphermaster.py
    ```

### Usage

After running the program, you’ll be prompted to enter plaintext and select an encryption algorithm by choosing a number between 1 and 6:

1. **Caesar Cipher**
2. **Vigenere Cipher**
3. **Affine Cipher**
4. **Hill Cipher**
5. **Substitution Cipher**
6. **One-Time Pad**

The program will then guide you through the steps required to encrypt and decrypt text with your chosen cipher.

### Example

**Encrypting with Caesar Cipher**

```plaintext
Enter the plaintext: HelloWorld
Choose an algorithm (1-6):
1. Caesar Cipher
2. Vigenere Cipher
3. Affine Cipher
4. Hill Cipher
5. Substitution Cipher
6. One-Time Pad
```
After choosing "1" for Caesar Cipher, you’ll enter a key to shift each character in the plaintext. The program will return the encrypted text and offer the option to decrypt it.

### Error Handling & Input Validation

CipherMaster handles invalid inputs gracefully by guiding you back to the previous steps or providing hints. If an invalid key is detected (e.g., in the Affine Cipher), the program will prompt you to re-enter a valid one.

### Contributing

If you’d like to contribute to CipherMaster, feel free to open an issue or submit a pull request. Any contributions are welcome to improve or expand the available ciphers.

### License

This project is licensed under the MIT License.
