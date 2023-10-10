def caesar_encryption(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    privare_key = 19
    encry_message = ""

    for c in msg:
        position = alphabet.find(c)
        new_position = (position + privare_key) % len(alphabet)
        new_character = alphabet[new_position]
        encry_message += new_character
    return encry_message


def caesar_decryption(msg, public_key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    private_key = 23
    decry_message = ""
    key = int(public_key / private_key)

    for c in msg:
        position = alphabet.find(c)
        new_position = (position - key) % len(alphabet)
        new_character = alphabet[new_position]
        decry_message += new_character
    return decry_message


def main():
    key = 437
    try:
        while True:
            message = input("Please enter a message: ")
            if message == "q":
                print("Goodbye!")
                break
            encry_message = caesar_encryption(message)
            decrypt_message = caesar_decryption(encry_message, key)
            print("Encrypted message: ", encry_message)
            print("Decrypted message: ", decrypt_message)
    except (KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
