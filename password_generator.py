import secrets
import string
import time

def slow_print(msg):
    for ch in msg:
        print(ch, end='', flush=True)
        time.sleep(0.02)
    print()

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return None  
    
    return ''.join(secrets.choice(chars) for _ in range(length))


def password():
    slow_print("Welcome\n")
    history = []

    while True:
        try:
            length = int(input("Enter desired password length (e.g. 12): "))
            if length < 4:
                slow_print("Password too short. Use at least 4 characters.")
                continue
        except ValueError:
            slow_print("Please enter a valid number.")
            continue

        use_upper = input("Include UPPERCASE letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        if not password:
            slow_print("Please select at least one character type.")
            continue
        slow_print("Generating your secure password...")
        time.sleep(0.5)
        
        slow_print(f"Your password is: {password}\n")
        history.append(password)
        # Ask for next action
        while True:
            choice = input("Generate another? (yes/no/view history): ").strip().lower()

            if choice == 'yes':
                break
            elif choice == 'no':
                slow_print(" Stay secure!")
                return
            elif choice == 'view history':
                slow_print("Passwords generated in this session:")
                for i, p in enumerate(history, 1):
                    print(f"   {i}. {p}")
            else:
                slow_print("Invalid input. Type yes, no, or view history.")

# Run
password()
