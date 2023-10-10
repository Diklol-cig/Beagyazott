from random import randint

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def generate_otp(characters):
    with open("otp.txt", "w") as f:
        for i in range(characters):
            f.write(str(randint(0, 26)) + "\n")


def load_otp():
    with open("otp.txt", "r") as f:
        contents = f.read().splitlines()
        return contents


def encrypt(message, key):
    result = []
    for i in range(len(message)):
        if message[i] not in ALPHABET:
            result.append(message[i])
        else:
            result.append(
                ALPHABET[(ALPHABET.find(message[i]) + int(key[i])) % len(ALPHABET)]
            )

    return "".join(result)


def decrypt(message, key):
    result = []
    for i in range(len(message)):
        if message[i] not in ALPHABET:
            result.append(message[i])
        else:
            result.append(
                ALPHABET[(ALPHABET.find(message[i]) - int(key[i])) % len(ALPHABET)]
            )

    return "".join(result)


def main():
    try:
        while True:
            message = input("Please enter a message: ")
            if message == "q":
                print("Goodbye!")
                break
            generate_otp(len(message))
            key = load_otp()
            encry_message = encrypt(message, key)
            decrypt_message = decrypt(encry_message, key)
            print("Encrypted message: ", encry_message)
            print("Decrypted message: ", decrypt_message)
    except (KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
