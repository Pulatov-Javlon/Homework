def addition(num1, num2):
    return num1+num2


def substraction(num1, num2):
    return num1-num2


def division(num1, num2):
    return num1/num2

def multiplication(num1, num2):
    return num1*num2


def main():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
        except:
            print("Please enter an integer for the first number!")
            continue
        else:
            print("Thanks for providing!")
            break
    while True:
        try:
            num2 = int(input("Enter the second number: "))
        except:
            print("Please enter an integer for the second number!")
            continue
        else:
            print("Thanks for providing!")
            break
    while True:
        try:
            math_type = input("Choose one of the options: \n+ || - || / or : || *\n  ")
        except:
            print("Please enter a valid option!")
            continue
        else:
            print("Thanks for providing!")
            break
    while math_type not in ['-', '+', '/', '*', ':']:
        math_type = input("Choose one of the options: \n+ || - || / or : || *\n  ")
        if math_type == '-':
            print(substraction(num1, num2))
            break
        elif math_type == '+':
            print(addition(num1, num2))
            break
        elif math_type == '/' or math_type == ':':
            print(division(num1, num2))
            break
        elif math_type == '*':
            print(multiplication(num1, num2))
            break
        else:
            continue













main()