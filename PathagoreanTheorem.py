import math
def main():
    num1 = float(input("Enter the length of side A: "))
    num2= float(input("Enter the length of side B: "))
    c = math.sqrt(num1*num1+num2*num2)
    print(f'The length of the hypotenuse is {c}')
main()

