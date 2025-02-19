import string

def caesar_cipher(text, shift, encrypt=True):
    result = []
    shift = shift if encrypt else -shift
    
    for char in text:
        if char in string.ascii_letters:
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

def main():
    while True:
        action = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()
        if action not in {'E', 'D'}:
            print("Invalid choice, try again.")
            continue
        
        message = input("Enter the text: ")
        try:
            shift_value = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Invalid shift value, must be an integer.")
            continue
        
        encrypted = action == 'E'
        output = caesar_cipher(message, shift_value, encrypted)
        print(f"Result: {output}\n")
        
        if input("Run again? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
