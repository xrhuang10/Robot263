from angles import theta, phi
import numpy as np

homex = float(input("Enter home x: "))
homey = float(input("Enter home y: "))

T1x = float(input("Enter T1 x: "))
T1y = float(input("Enter T1 y: "))
T2x = float(input("Enter T2 x: "))
T2y = float(input("Enter T2 y: "))
T3x = float(input("Enter T3 x: "))
T3y = float(input("Enter T3 y: "))

A1x = T1x - 30
A2x = T2x - 30
A3x = T3x - 30
A1y = T1y
A2y = T2y
A3y = T3y

move_sequence = [1, 2, 3, 2, 3, 1]


for i in move_sequence:
    if i == 1:
        x = A1x
        y = A1y
        ##open gripper
        ##delay 1sec
        x = T1x
        y = T1y

    elif i == 2:
        x = A2x
        y = A2y
    elif i == 3:
        x = A3x
        y = A3y
    print("Theta = " + str(theta(x, y)) + " degrees")
    print("Phi = " + str(phi(x, y)) + " degrees")
    print("Move to next position")