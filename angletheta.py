import math
def main():
    num1 = float(input("Enter the length of side A: "))
    num2= float(input("Enter the length of side B: "))
    c = math.sqrt(num1*num1+num2*num2)
    print(f'The length of the hypotenuse is {c}')
main()

y= num1
x= num2

def theta():
    theta = math.atan2(y,x) 
    Degrees = theta * (180 / 3.14)
    print(f'The degress for the right triangle {Degrees}')
theta()
