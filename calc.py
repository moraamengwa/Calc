def add (num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'you cannot devide a number with zero!!'

num1 = input("Enter your first number... ")
num2 = input("Enter your second number... ")

print ("Please enter the number of an option below...\n")
print("1: Addition\n")
print("2: Subtraction\n")
print("3: Multiplication\n")
print("4: Division\n")

opt = input()

print("\n")
if opt == 1:
    print("The answer is: {}").format(add(num1, num2))
elif opt == 2:
    print("The answer is: {}").format(sub(num1, num2))
elif opt == 3:
    print("The answer is: {}").format(mul(num1, num2))
elif opt == 4:
    print("The answer is: {}").format(div(num1, num2))
else:
    print("OOPS!! That option does not exist!")
