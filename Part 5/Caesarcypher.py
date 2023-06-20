import string

class Caesarcypher:
    def __init__(self, shift, text):
        self.shift = shift
        self.text = text
        self.cipher = self.create_dictionary()

    # Function to create a dictionary for the caesarcypher
    def create_dictionary(self):
        # String of english letters alphabet
        alphabet = string.ascii_lowercase
        
        # Dictionary to store the encryption
        decryption_dict = {}

        # Loop through the alphabet
        for i in range(len(alphabet)):
            # Calculate the decrypted letter
            decrypted_letter = alphabet[(i - self.shift) % 26]

            # Add the decrypted letter to the dictionary
            decryption_dict[alphabet[i]] = decrypted_letter
            decryption_dict[alphabet[i].upper()] = decrypted_letter.upper()

        return decryption_dict
        
    # Function to decrypt the text using dictionary
    def decypher(self):
        decrypted = ""

        # For every character in the text
        for char in self.text:
            # If the character is a letter
            if char.isalpha():
                # Decrypt the character
                decrypted_char = self.cipher[char]
                # Add the decrypted character to the decrypted text
                decrypted += decrypted_char
            else:
                # Add the character to the decrypted text
                decrypted += char
        return decrypted
    
    def decypher_calculation(self):
        decrypted = ""

        # For every character in the text
        for char in self.text:
            # If the character is a letter
            if char.isalpha():
                # Calculate letter ASCII value
                if char.isupper():
                    decrypted_char = chr((ord(char) - self.shift - 65) % 26 + 65)
                else:
                    decrypted_char = chr((ord(char) - self.shift - 97) % 26 + 97)
                # Add the decrypted character to the decrypted text
                decrypted += decrypted_char
            else:
                # Add the character to the decrypted text
                decrypted += char
        return decrypted