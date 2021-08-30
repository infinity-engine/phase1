import matplotlib.pyplot as plt
import math
import random

# Global Variables and Data Structures

# Let make a Queue(data structure) which will store the recent x values and corresponding functionvalues
# we will only store 3 values at this point


class CustomQueue:
    def __init__(self) -> None:
        self.x_values = []
        self.function_values = []

    def push_x_and_f_value(self, x, f):
        # x is the point and f=function(x)
        self.x_values.append(x)
        self.function_values.append(f)

        # now pope the first item from both the que
        if(len(self.x_values) > 3):
            self.x_values.pop(0)
            self.function_values.pop(0)
        else:
            pass


objectiveFunctionIndicator = 1
epsinol = 10**-3
delta = 0.0198
lowerLimit = -10
upperLimit = 0.5
noOf_functionEval = 0
myQ_1 = CustomQueue()  # Queue

# Initiate the Optimization Method Here
def start():
    # take input from the user and run the methods


    #set no of function evaluation = 0
    global noOf_functionEval
    noOf_functionEval = 0

    global myQ_1
    #reinitialise the queue
    myQ_1 = CustomQueue()
    [a, b] = boundingPhaseMethod(lowerLimit, upperLimit)
    print(f"Bounding Phase Method -> {a} to {b}")
    print(f"No of function evaluations at the end of Bracketing Method = {noOf_functionEval}")

    #reinitialise the queue
    myQ_1 = CustomQueue()
    [a, b] = intervalHalving(a, b)
    print(f"Interval Halving Method -> {a} to {b}")
    print(f"Total no of function evaluations = {noOf_functionEval}")


# Bracketing Method
def boundingPhaseMethod(a, b):
    k = 0
    deltaWithSign = 0
    while True:
        # step 1
        x_0 = random.uniform(a, b)
        if (x_0 == a or x_0 == b):
            continue

        # step 2
        if objectiveFunction(x_0 - abs(delta)) >= objectiveFunction(x_0) and objectiveFunction(x_0 + abs(delta)) <= objectiveFunction(x_0):
            deltaWithSign = + abs(delta)
        elif objectiveFunction(x_0 - abs(delta)) <= objectiveFunction(x_0) and objectiveFunction(x_0 + abs(delta)) >= objectiveFunction(x_0):
            deltaWithSign = - abs(delta)
        else:
            continue

        while True:
            # step 3
            x_new = x_0 + 2**k*deltaWithSign

            if objectiveFunction(x_new) < objectiveFunction(x_0):
                k += 1
                x_0 = x_new
                continue
            else:
                return [x_new-(2**k)*1.5*deltaWithSign, x_new]


# Bounding Phase method
def intervalHalving(a, b):
    # step 1
    x_m = (a+b)/2
    l = b-a
    no_of_iteration = 1

    while True:
        # step2
        x_1 = a+l/4
        x_2 = b-l/4

        while True:
            # step3
            if objectiveFunction(x_1) < objectiveFunction(x_m):
                b = x_m
                x_m = x_1
                break

            # step4
            if objectiveFunction(x_2) < objectiveFunction(x_m):
                a = x_m
                x_m = x_2
                break
            else:
                a = x_1
                b = x_2
                break

        # step5
        l = b-a
        if l < epsinol:
            return [a, b]
            break
        else:
            continue


# Objective functions' definition
def objectiveFunction(x):
    #check whther the x is already stored in the queue
    global noOf_functionEval
    if (x in myQ_1.x_values):
        return (myQ_1.function_values[myQ_1.x_values.index(x)])
    else:
        noOf_functionEval += 1
        if (objectiveFunctionIndicator == 1):
            value = (x**2-1)**3-(2*x-5)**4
        elif(objectiveFunctionIndicator == 2):
            pass
        elif(objectiveFunctionIndicator == 3):
            pass
        elif(objectiveFunctionIndicator == 4):
            pass
        elif(objectiveFunctionIndicator == 5):
            pass
        elif(objectiveFunctionIndicator == 6):
            pass

    myQ_1.push_x_and_f_value(x,value)
    return value


# Run the code from here.
start()
