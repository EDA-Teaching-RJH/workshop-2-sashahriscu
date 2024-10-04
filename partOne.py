# task: implement a program that prompts the user for input and then outputs that same input replacing each space with three periods

# define principal function
def main():
# prompt user to input a line of text
    slow = input("Input ")
    replace(slow)

# define function to replace the whitespaces
def replace(text):
# strip function to remove whitespaces in the input string
  slow = text.strip()
# replace the blank spaces in input with 3 periods
  result = slow.replace(" ", "...")
# print the output. output being whitespace replaced with three periods
  print(result)

# call on main to run function
main()