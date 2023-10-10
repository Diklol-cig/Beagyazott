

def caesar(msg, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_msg = ''
    for c in msg:
        position = alphabet.find(c)
        new_position = (position + key) % len(alphabet)
        new_character = alphabet[new_position]
        if c.isupper():
            new_character = new_character.upper()
        else:
            new_character = new_character.lower()
        new_msg += new_character
    return new_msg




def main():
    key = 3
    try:
        while True:
            message = input('Please enter a message: ')
            if message == 'q': print('Goodbye!');break 
            encry_message = caesar(message, key)
            print('Encrypted message: ', encry_message)
    except(KeyboardInterrupt):
        print('\nGoodbye!')
        
    
    
    
if __name__ == "__main__":
    main()

