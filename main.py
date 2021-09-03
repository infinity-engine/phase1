from typing import List
import matplotlib.pyplot as plt
import math
import random

# Global Variables and Data Structures
objectiveFunctionIndicator = 1
epsinol = 10**-3
delta = 0.0198
lowerLimit = -10
upperLimit = 0.5
noOf_functionEval = 0
queueSize = 5
myQ_1 = None  # Queue
out = open(r"Phase_1_iterations.out", "w")

#Bounding Phase Method varibales for ploting
x_series = []
f_x_series = []
x_1_series = []
f_x_1_series = []
x_2_series =[]
f_x_2_series = []

#Interval Halving Method Variables for ploting
x_m_series = []
f_x_m_series = []

# Let make a Queue(data structure) which will store the recent x values and corresponding function values
# we will only store limited values at this point
class CustomQueue:
    global queueSize
    def __init__(self) -> None:
        self.x_values = []
        self.function_values = []

    def push_x_and_f_value(self, x, f):
        # x is the point and f=function(x)
        self.x_values.append(x)
        self.function_values.append(f)

        # now pope the first item from both the que
        if(len(self.x_values) > queueSize):
            self.x_values.pop(0)
            self.function_values.pop(0)
        else:
            pass


# Initiate the Optimization Method Here
def start():
    # take input from the user and run the methods
    global out,noOf_functionEval,myQ_1

    #set no of function evaluation = 0
    noOf_functionEval = 0
    
    #reinitialise the queue
    myQ_1 = CustomQueue()
    [a, b] = boundingPhaseMethod(lowerLimit, upperLimit)
    
    print(f"Bounding Phase Method -> {a} to {b}")
    print(f"No of function evaluations at the end of Bracketing Method = {noOf_functionEval}")
    
    plt.figure(1)
    plt.title("Bounding Phase Method")
    plt.xlabel("x in various iterations")
    plt.ylabel("F(x) in various Iterations")
    plt.plot(x_series,f_x_series,"r*-")
    

    #re-initialise the queue
    myQ_1 = CustomQueue()
    
    out.write("\n\n")
    
    #call the region elimination method
    [a, b] = intervalHalving(a, b)
    
    print(f"Interval Halving Method -> {a} to {b}")
    print(f"Total no of function evaluations = {noOf_functionEval}")
    
    plt.figure(2)
    plt.title("Interval Halving Method")
    plt.xlabel("x_m in various iterations")
    plt.ylabel("F(x_m) in various iterations")
    plt.plot(x_m_series,f_x_m_series,"b+-")
    
    plt.show()


# Bracketing Method
def boundingPhaseMethod(a, b):
    global out,x_series,f_x_series
    
    #Write in the output File
    out.write("Bounding Phase Method - Results\n")
    out.write("#Iteration\t\t\tx\t\t\t\t\tf(x)\n")
    
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
        
        #Write the initial value of x and f(x)
        out.write("{}\t\t\t{}\t\t{}\n".format(k,x_0,objectiveFunction(x_0)))
        
        #Fill the data in the List for ploting
        x_series.append(x_0)
        f_x_series.append(objectiveFunction(x_0))

        while True:
            # step 3
            x_new = x_0 + 2**k*deltaWithSign

            if objectiveFunction(x_new) < objectiveFunction(x_0):
                k += 1
                x_0 = x_new
                #write the new value of x and f(x)
                out.write("{}\t\t\t{}\t\t{}\n".format(k,x_new,objectiveFunction(x_new)))
                
                #Fill the data in the List for ploting
                x_series.append(x_new)
                f_x_series.append(objectiveFunction(x_new))
                continue
            else:
                return [x_new-(2**k)*1.5*deltaWithSign, x_new]


# Bounding Phase method
def intervalHalving(a, b):
    global x_m_series,f_x_m_series
    
    # step 1
    x_m = (a+b)/2
    l = b-a
    no_of_iteration = 1
    
    #Write in the output File
    out.write("Interval Halving Method - Results\n")
    out.write("#Iteration\t\t\tx_1\t\t\t\t\tx_m\t\t\tx_2\t\t\t\t\tf(x_1)\t\t\t\t\tf(x_m)\t\t\t\t\tf(x_2)\n")
    
    #Write the initial value of x and f(x)
    out.write("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t{}\n".format(no_of_iteration,a,x_m,b,objectiveFunction(a),objectiveFunction(x_m),objectiveFunction(b)))
    
    #Fill the data in the store as well
    x_m_series.append(x_m)
    f_x_m_series.append(objectiveFunction(x_m))

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
        #Write the value of x and f(x)
        out.write("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t{}\n".format(no_of_iteration,a,x_m,b,objectiveFunction(a),objectiveFunction(x_m),objectiveFunction(b)))
    
        #Fill the data in the store as well
        x_m_series.append(x_m)
        f_x_m_series.append(objectiveFunction(x_m))
        
        l = b-a
        if l < epsinol:
            return [a, b]
            break
        else:
            no_of_iteration += 1
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
