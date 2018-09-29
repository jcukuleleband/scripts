import sys
sys.path.append('../CException/') #https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3

import CException

def main():
	#Test 1: Throw an execption with a message.  Catch CException, read message.
        try:
            print ("Test #1:")
            raise CException("Raising Error 1")
        except:
            print (CException.message())



if __name__ == "__main__":
    main()
