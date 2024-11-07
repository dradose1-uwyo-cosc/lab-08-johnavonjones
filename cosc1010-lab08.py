# Johnavon Jones
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to:
# 

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them
def check_string(string):
    """Checks string to see if it is an int or float"""
    try:
        if str(int(string)) == string:
            return int(string)
    except ValueError:
        pass

    try:
        if str(float(string)) == string:
            return float(string)
    except ValueError:
        return False


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
def slope_intercept(m, b, L, H):
    """Returns a list of all values of y for the given x range"""
    if L <= H:
        try:
            L = int(L)
            H = int(H)
            values = []
            for x in range(L, H+1):
                y = (m*x) + b
                values.append((x, y))
            return values
        except:
            return False
    else:
        return False
    
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
while True:
    user_input = input("Input the slope, y-intercept point, and the upper and lower bounds with commas between each \n(Type 'Exit' to stop):")
    if user_input.lower() == "exit":
        break

    user_input = user_input.strip(" ")
    user_input = user_input.split(",")
    try:
        m = float(user_input[0])
        b = float(user_input[1])
        L = int(user_input[2])
        H = int(user_input[3])
        result = slope_intercept(m, b, L, H)  
        print(f"The coordinates of your parameters are: {result}")
    except (ValueError, IndexError):  
        print("Invalid input. Please enter numeric values for the slope, y-intercept, and bounds.")
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadratic_formula(a, b, c):
    square_root = (b*b) - 4*a*c
    if square_root > 0:
        x1 = (-b + (square_root ** 0.5))/(2*a)
        x2 = (-b - (square_root ** 0.5))/(2*a)
        return x1, x2
    elif square_root == 0:
        x = -b / (2*a)
        return x, x
    elif square_root < 0:
        return "null"
    
def square_root_operation(a, b, c):
    square_root = (b*b) - 4*a*c
    if square_root > 0:
        root = (square_root ** 0.5)
        return root
    elif square_root == 0:
        return 0
    elif square_root < 0:
        return "null"
    
while True:
    user_input = input("Input the a, b, and c values with commas between, and I will calculate the 0's of the function using the Quadratic Equation \n(Type 'Exit' to stop):")
    if user_input.lower() == "exit":
        break

    user_input = user_input.strip(" ")
    user_input = user_input.split(",")
    
    try:
        a = float(user_input[0])
        b = float(user_input[1])
        c = float(user_input[2])
        if quadratic_formula(a, b, c) != "null":
            print(f"The zero(s) are {quadratic_formula(a, b, c)[0]} and {quadratic_formula(a, b, c)[1]}")
        else:
            print(f"That function has no real zeroes.")
    except:
        print("Invalid Inputs. Please enter numerical values.")