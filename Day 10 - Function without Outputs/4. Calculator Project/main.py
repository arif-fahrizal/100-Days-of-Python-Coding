from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)

    should_accumulate = True
    num1 = float(input("First Number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an Operations: ")
        num2 = float(input("First Number: "))

        answer = operations[operations_symbol](num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 10)
            calculator()

calculator()