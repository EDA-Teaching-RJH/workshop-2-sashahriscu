#define principal function
def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")

def pounds_to_float(d):
# taking decimal d and returning it as a float with £ emitted
    return float(d.strip("£"))

def percent_to_float(p):
# taking percentage P and returning it as a float decimal (hence /100) with % emitted
    return float(p.strip("%"))/100

# call on main to perform function
main()
