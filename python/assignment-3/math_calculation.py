import math

# 1.   Asks the user for a number as input.
num = int(input("Enter a number: "))

#2.   Uses the math module to calculate the:

#o   Square root of the number
sqrt_num = math.sqrt(num)

#o   Natural logarithm (log base e) of the number
log_num = math.log(num)

#o   Sine of the number (in radians)
sin_num = math.sin(num)


#3.   Displays the calculated results.
print(f"Square root of {num} is: {sqrt_num}")
print(f"Natural logarithm of {num} is: {log_num}")
print(f"Sine of {num} is: {sin_num}")
