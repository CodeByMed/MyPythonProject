import random
import string


class SimpleEncryptor:
    def __init__(self):
        """
        Initialize the SimpleEncryptor class.
        - Generates a shuffled key to map characters for encryption and decryption.
        """
        # Define the character set (space, punctuation, digits, and letters)
        self.chars = " " + string.punctuation + string.digits + string.ascii_letters
        self.chars = list(self.chars)
        self.key = self.chars.copy()

        # Shuffle the key to randomize the mapping
        random.shuffle(self.key)

    def encrypt(self, plain_text):
        """
        Encrypt the given plaintext message using a shuffled character set.
        """
        cipher_text = ""
        for letter in plain_text:
            if letter in self.chars:
                index = self.chars.index(letter)
                cipher_text += self.key[index]
            else:
                raise ValueError(f"Character '{letter}' is not in the valid character set.")
        return cipher_text

    def decrypt(self, cipher_text):
        """
        Decrypt the given cipher text message using the shuffled key.
        """
        plain_text = ""
        for letter in cipher_text:
            if letter in self.key:
                index = self.key.index(letter)
                plain_text += self.chars[index]
            else:
                raise ValueError(f"Character '{letter}' is not in the encrypted character set.")
        return plain_text


def main():
    encryptor = SimpleEncryptor() # Create Instance of SimpleEncryptor Class.

    # ENCRYPTION
    plain_text = input("Enter a message to encrypt: ")
    encrypted_message = encryptor.encrypt(plain_text)
    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {encrypted_message}")

    # DECRYPTION
    cipher_text = input("Enter a message to decrypt: ")
    decrypted_message = encryptor.decrypt(cipher_text)
    print(f"Encrypted message: {cipher_text}")
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
