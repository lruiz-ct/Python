mass = float (input("Enter object's mass:"))
weight = mass * 9.8

if weight < 100:
    print ("Object is too light")
elif weight > 500:
    print ("Object is too heavy")
