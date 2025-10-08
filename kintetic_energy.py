mass = float(input("What's your mass?: "))
velocity = int(input("What's your velocity?: "))

def kinetic_energy(mass, velocity):
    ke = .5 * mass * (velocity ** 2)
    print(f"Your mass is {mass}, your velocity is {velocity}, and your kentic enegry is {ke}.")
kinetic_energy(mass, velocity)