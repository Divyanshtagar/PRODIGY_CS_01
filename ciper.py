# caesar_cipher.py

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The input message to be encrypted or decrypted.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""
    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            result += shifted_char
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            start = ord('A')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            result += shifted_char
        else:
            # Keep non-alphabetic characters as they are
            result += char
    return result

def main():
    """
    Main function to run the Caesar Cipher program.
    Allows user input for message, shift, and mode (encrypt/decrypt).
    """
    print("Welcome to the Caesar Cipher Program!")

    while True:
        message = input("\nEnter your message: ")
        
        # Validate shift value input
        while True:
            try:
                shift = int(input("Enter the shift value (an integer): "))
                break
            except ValueError:
                print("Invalid shift value. Please enter an integer.")

        # Validate mode input
        while True:
            mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
            if mode in ['e', 'encrypt']:
                mode_str = "encrypt"
                break
            elif mode in ['d', 'decrypt']:
                mode_str = "decrypt"
                break
            else:
                print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

        processed_message = caesar_cipher(message, shift, mode_str)

        if mode_str == "encrypt":
            print(f"\nEncrypted message: {processed_message}")
        else:
            print(f"\nDecrypted message: {processed_message}")

        # Ask if the user wants to perform another operation
        another_go = input("\nDo you want to perform another operation? (yes/no): ").lower()
        if another_go != 'yes':
            print("Thank you for using the Caesar Cipher Program! Goodbye.")
            break

if __name__ == "__main__":
    main()
