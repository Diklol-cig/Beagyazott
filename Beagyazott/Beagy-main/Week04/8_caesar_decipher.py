def caesar_decryption(message):
    alphabet = "".join([chr(i) for i in range(ord("a"), (ord("z") + 1))])


def main():
    try:
        while True:
            message = input("Please enter a message: ")
            if message == "q":
                print("Goodbye!")
                break
            (decrypt_message, key) = caesar_decryption(message)
            print("Decrypted message: ", decrypt_message)
            print("Key: ", key)
    except (KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
