import time

def calc (a, b):
    val = input(str(a) + " - " + str(b) + " = ")
    if val != a-b:
        print ("Wrong")
        calc(a,b)
    return

def main():
    start_time = time.time()
    calc(18,8)
    calc(8,8)
    calc(11,8)
    calc(17,8)
    calc(15,8)
    calc(12,8)
    calc(14,8)
    calc(13,8)
    calc(16,8)
    calc(9,8)
    calc(19,8)
    calc(10,8)
    end_time = time.time()
    print(str(round(end_time-start_time, 1)) + " seconds")
   
    


if __name__ == '__main__':
    main()
