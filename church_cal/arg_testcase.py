#!/usr/bin/env python3

import sys

def main():

    print ("The script has the name %s" % (sys.argv[0]) )
    
    # count the arguments
    arguments = len(sys.argv) - 1 
    print ("the script is called with %i arguments" % (arguments))  

    # output argument-wise
    position = 1  
    while (arguments >= position):  
        print ("parameter %i: %s" % (position, sys.argv[position]))
        position = position + 1

  

if __name__ == '__main__':
    main()
