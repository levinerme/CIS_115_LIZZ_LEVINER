import math
def calucating_theta(num1, num2):
    theta = math.atan2(num1, num2)
    thetaDegrees = theta * (180/math.pi)
    print(f" Theta is {thetaDegrees} degrees.")
calucating_theta()

  