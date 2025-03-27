#X is the shortest distance from the gripper to metal bar
#Y is the distance from the gripper to the phi motor parallel to the metal bar

#l1 is the length of the bar attached to the theta motor
#l2 is the length of the bar connecting l1 tip to the gripper
#l3 is the length of l2 but cut off where it meets l4
#l4 is the length of the bar connecting l5 tip and l3 tip (intersecting l2)
#l5 is the length of the bar attached to the phi motor
#dmotor is the separation between the theta and phi motors

import numpy as np

l1 = 83.55
l2 = 180
l3 = 73.29
l4 = 166
l5 = 83.55

dmotor = 94.13

def thetaprime(x, y):
    numerator = x * x + pow(dmotor - y, 2) - l1 * l1 - l2 * l2
    denominator = -2 * l1 * l2
    thetaprime = np.degrees(np.arccos(numerator/denominator))
    return thetaprime


def theta(x, y):
    theta2 = np.degrees(np.arcsin((l2*(np.sin(np.radians(thetaprime(x, y))))) / (np.sqrt(l1*l1 + l2*l2 - 2*l1*l2*(np.cos(np.radians(thetaprime(x, y))))))))
    theta3 = np.degrees(np.arctan(x / (dmotor - y)))
    # print(thetaprime(x, y))
    # print(theta2)
    # print(theta3)
    return (180 - theta2 - theta3)



def phi(x, y):
    e = l1*np.sin(np.radians(theta(x, y)))
    f = l3*np.cos(np.radians(90 + theta(x, y) - thetaprime(x, y)))
    x2 = e + f

    d = l1*np.cos(np.radians(theta(x, y)))
    g = l3*np.sin(np.radians(90 + theta(x, y) - thetaprime(x, y)))
    y2 = dmotor + d - g
    def phi1():
        answer = np.degrees(np.arctan(x2 / y2))
        return answer
    
    def phi2():
        #h is the distance between the phi motor point and the gripper
        h = np.sqrt(x2*x2 + y2*y2)
        answer = np.degrees(np.arccos((l4*l4 - h*h - l5*l5) / (-2*h*l5)))
        return answer
    
    return phi1() + phi2()


while True:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Theta = " + str(theta(x, y)) + " degrees")
    print("Phi = " + str(phi(x, y)) + " degrees")
    print(" ")


