#-------------------------------------------------------------
# Simple python script to help child with practicing
# Mad Minute Math

#-------------------------------------------------------------
# Import Statements
import time
import random

#-------------------------------------------------------------
# Function for calculating a + b where a and b are integers
def calc_add (a, b):
    try:
        val = input(str(a) + " + " + str(b) + " = ")

        if int(val) != int(a+b):
            print ("Wrong")
            calc_add(a,b)
    except:
        calc_add(a,b)
    return

#-------------------------------------------------------------
# Function for calucating a - b where a and b are integers
def calc_minus (a, b):
    try:
        val = input(str(a) + " - " + str(b) + " = ")

        if int(val) != int(a-b):
            print ("Wrong")
            calc_minus(a,b)
    except:
        calc_minus(a,b)
    return

#-------------------------------------------------------------
# Function for calculating a * b where a and b are integers
def calc_mult (a, b):
    try:
        val = input(str(a) + " x " + str(b) + " = ")

        if int(val) != int(a*b):
            print ("Wrong")
            calc_mult(a,b)
    except:
        calc_mult(a,b)
    return

#-------------------------------------------------------------
# Return a random int between x and y and not equal to z
def random_int_value(x,y,z):
    val =  random.randint(x-5,y+5)  #TODO (5): larger deviation with +/- 5.  There is a need to analyze the effectiveness of this methodology
    #if (val == z) or ((val < x) or (val > y)):
    if (val == z) or (val < x) or (val > y):
        val = random_int_value(x,y,z)
    return val

#-------------------------------------------------------------
# Main Function
def main():

    # TODO (3): Consider in future moving guts of Main
    # to a function or class for modularity purposes

    #Setup
    a = 8  #Lower Range
    b = 19 #Upper Range
    num = 8 # ie. minus 8s
    iterations = 10 #Number of times to loop
    #
    # TODO (1): In the future consider adding a switch for
    # the type of operation desired.  Also consider
    # using command line parameters to define the Setup
    #

    start_time = time.time()
    val = 0 #Set initial value for val. Perhaps in future should be Max integer

    for i in range(iterations):
        val = random_int_value(a,b,val);
        #
        #TODO (2): Consider in future add switch based on TODO #1
        #
        calc_minus(val,num)
        #calc_mult(val,num)
        #calc_add(val,num)
    end_time = time.time()

    print(str(round(end_time-start_time, 1)) + " seconds")

    input("Press any Enter Key to end")

#-------------------------------------------------------------
# Main Declaration
if __name__ == '__main__':
    main()
