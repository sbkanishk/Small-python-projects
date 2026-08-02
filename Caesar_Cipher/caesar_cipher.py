def caesar(text, shift, direction):
    result = ""

    # Reverse the shift for decryption
    if direction == "d":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Preserve uppercase and lowercase letters
            if char.islower():
                start = ord("a")
            else:
                start = ord("A")

            # Shift the letter and wrap around using modulo
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep spaces, numbers, and symbols unchanged
            result += char

    return result


print("=== Caesar Cipher ===")

while True:
    direction = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if direction not in ["e", "d"]:
        print("Invalid choice! Please enter 'e' or 'd'.\n")
        continue

    text = input("Enter your message: ")

    try:
        shift = int(input("Enter shift number: ")) % 26
    except ValueError:
        print("Shift must be a number.\n")
        continue

    output = caesar(text, shift, direction)

    if direction == "e":
        print(f"\nEncrypted Message: {output}")
    else:
        print(f"\nDecrypted Message: {output}")

    again = input("\nDo you want to continue? (y/n): ").lower()

    if again != "y":
        print("Goodbye!")
        break