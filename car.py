#!/usr/bin/env python

class Vehicle:
    wheels = 4
    def __init__(self):
        print("vehicle")
    def calcVelocity(self,x):
        return 3*x+10

class Car(Vehicle):
    def __init__(self):
        self.speed = 10

slowcar = Car()
print(slowcar.speed)
print(slowcar.calcVelocity(20))
print(slowcar.wheels)