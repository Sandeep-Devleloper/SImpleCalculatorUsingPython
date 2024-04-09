currentValue = 0
nextElement = 0
number = int(input("Enter a number: "))
i = 0

while True:
    operator = input("Select exit(e) or an operation (+,-,*,/,%): ").lower()
    
    if operator == "e":
        break
    
    if operator in ["+", "-", "*", "/", "%"]:
        nextElement = int(input("Enter next number: "))
        
        if operator == "+":
            if i == 0:
                currentValue = number + nextElement
            else:
                currentValue += nextElement
            print(f"Sum = {currentValue}")
        
        elif operator == "-":
            if i == 0:
                currentValue = number - nextElement
            else:
                currentValue -= nextElement
            print(f"Subtraction = {currentValue}")
        
        elif operator == "*":
            if i == 0:
                print("0*anything = 0")
            else:
                currentValue *= nextElement
            print(f"Multiplication = {currentValue}")
        
        elif operator == "/":
            if nextElement == 0:
                print("Error: Division by zero is not allowed.")
            else:
                currentValue /= nextElement
            print(f"Division = {currentValue}")
        
        elif operator == "%":
            if nextElement == 0:
                print("Error: Modulo operation requires a non-zero divisor.")
            else:
                currentValue %= nextElement
            print(f"Modulo = {currentValue}")
        
        i += 1
    else:
        print("Invalid operator. Please try again.")
