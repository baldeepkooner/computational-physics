import math

def satelliteAltitude():
    G = 6.67 * math.pow(10, -11)
    M = 5.97 * math.pow(10, 24)
    R = 6371
    T = 0
    while T <= 0 :
        T = input("Please enter time of orbit of satellite (seconds): ")
    print "\n"
    h = math.pow(((G*M*math.pow(T, 2)) / ((4 * (math.pow(math.pi, 2))))), (1.0/3.0)) - R
    if h > 160000 and h < 2000000:
        print "The satellite must orbit at an altitude (meters) of: ", h
        print "The satellite is in Low Earth Orbit.\n"
    elif h > 35786000:
        print "The satellite must orbit at an altitude (meters) of: ", h
        print "The satellite is in High Earth Orbit.\n"
    elif h < 160000:
        print "The satellite must orbit at an altitude (meters) of: ", h
        print "The satellite will experience rapid orbital decay and altitude loss.\n"
    else:
        print "The satellite must orbit at an altitude (meters) of: ", h
        print "The satellite is in Medium Earth Orbit.\n"

def quad(a, b, c):
    r2 = ((-1) * b + math.sqrt(math.pow(b, 2) - 4*a*c)) / 2*a
    return r2

def planetaryOrbits():
    G = 6.67 * math.pow(10, -11)
    M = 1.9891 * math.pow(10, 30)
    l1 = 0
    while l1 <= 0:
        l1 = input("Please enter perihelion distance (m): ")
    v1 = 0
    while v1 <= 0:
        v1 = input("Please enter perihelion linear velocity (m/s): ")
    print "\n"
    v2 = quad(1, -(2*G*M) / (v1*l1), math.pow(v1, 2) - (2*G*M)/l1)
    l2 = (l1*v1) / v2
    a = 0.5*(l1+l2)
    b = math.sqrt(l1 * l2)
    T = (2 * math.pi * a * b) / (l1 * v1)
    e = (l2 - l1) / (l2 + l1)
    print "Orbital Period: ", T, "\n"
    print "Orbital eccentricity: ", e, "\n"

def semiEmpiricalMass():
    Z = 0
    while Z <= 0:
        Z = input("Please enter an atomic number: ")
    A = 0
    while A <= 0:
        A = input("Please enter a mass number: ")
    print "\n"
    a1, a2, a3, a4 = 15.67, 17.23, 0.75, 93.2
    if A%2 != 0:
        a5 = 0
    elif A%2 == 0 and Z%2 == 0:
        a5 = 12.0
    else:
        a5 = -12.0
    B = a1*A - (a2 * math.pow(A, 2.0/3.0) - (a3*(math.pow(Z, 2) / math.pow(A, 1.0/3.0)) - (a4 * (math.pow((A - 2*Z), 2) / A)) + (a5 / math.sqrt(A))))
    print "The nuclear binding energy for the corresponding atom is: ", B, "\n"



print "1) Satellite Altitude\n2) Planetary Orbits\n3) Semi-Empirical Mass\n"
k = 0
while k != 1:
    option = input("Choose an option: ")
    print "\n"
    if option == 1:
        satelliteAltitude()
        print "\n"
    elif option == 2:
        planetaryOrbits()
        print "\n"
    elif option == 3:
        semiEmpiricalMass()
        print "\n"
    else:
        print "Invalid input. Please enter the number corresponding to your desired option.\n"
    k = input("Press 1 to exit, 0 to continue. ")
    print "\n"


