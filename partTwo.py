import math

# define principal function
def main():
# prompt user input for sides A and B, float used for decimal numbers
    A = float(input("What is the length of side A? "))
    B = float(input("What is the length of side B? "))
# define 'C' or the hypotenuse
    pythag(A,B)
# print result of the hypotenuse
    print(f"The length of the hypotenuse is: {(pythag(A,B))}")

# define result
def pythag(A,B):
# square rooting to return C result
    return math.sqrt((A**2) + (B**2))
    
# call on main to perform function
main()