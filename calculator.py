"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
while True:
    # read input
    print("Please enter an operator and numbers (or type 'q' to quit)")
    user_input = input("> ")

    # check if user asked to quit
    if user_input == "q":
        print("Okay, you are exiting!")
        break

    # otherwise, keep going... #
    user_input_split = user_input.split(" ") 


    # tokenise input V2
    # only one number expected if cube or square
    if len(user_input_split) == 2:
        operator, num1 = user_input_split
        num1 = float(num1)

    if len(user_input_split) == 3: 
        operator, num1, num2 = user_input_split 
        num1 = float(num1)
        num2 = float(num2)


    # run various operators
    if operator == "+": 
        print (add(num1, num2))

    elif operator == "-":
        print (subtract(num1, num2))

    elif operator == "*":
        print (multiply(num1, num2)) 

    elif operator == "/":
        print (divide(num1, num2)) 

    elif operator == "square":
        print (square(num1))

    elif operator == "cube":
        print (cube(num1))

    elif operator == "power":
        print (power(num1, num2))
    
    elif operator == "mod":
        print (mod(num1, num2))

    else: 
        print("Unrecognised operator. Please use only one of the following:")
        print("+ - * / square cube power mod")
