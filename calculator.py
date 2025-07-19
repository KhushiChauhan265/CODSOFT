import time

def slow_print(msg):
    for ch in msg:
        print(ch, end='', flush=True)
        time.sleep(0.02)
    print()

def calculator():
    slow_print("Welcome\n")
    history = []

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Choose operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    slow_print("Division by zero is not valid")
                    continue
                result = num1 / num2
            else:
                slow_print("Invalid operation. Use only +, -, *, /.")
                continue

            slow_print(f"The result is: {result}\n")
            history.append(f"{num1} {operator} {num2} = {result}")

        except ValueError:
            slow_print("INvalid Number!")
            continue

        while True:
            choice = input("Want to do another calculation? (yes/no/view history): ").strip().lower()

            if choice == 'yes':
                break  
            elif choice == 'no':
                slow_print("ThankYou!")
                return
            elif choice == 'view history':
                slow_print("Your Calculation History:")
                for h in history:
                    print(h)
                
            else:
                slow_print("Invalid input. Please type yes, no, or view history.")

# Run
calculator()
