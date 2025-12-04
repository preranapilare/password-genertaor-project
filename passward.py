import string
import secrets

def generate_password(length, use_digits=True, use_symbols=True):
    # Base character set: letters
    characters = string.ascii_letters

    if use_digits:
        characters += string.digit
    if use_symbols:
        characters += string.punctuation

    # Check for valid length
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Secure password generation using secrets (cryptographically strong)
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_digits, use_symbols)
        print("\n✅ Your Generated Password:", password)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
