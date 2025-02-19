def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

if __name__ == "__main__":
    while True:
        mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}\n")
        
        another = input("Do you want to process another message? (yes/no): ").strip().lower()
        if another != 'yes':
            break
