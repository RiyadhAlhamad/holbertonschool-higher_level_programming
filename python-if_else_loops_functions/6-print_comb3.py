#!/usr/bin/python3
for n in range(10):
    for i in range(10):
        if(n is 8 and i is 9):
            print("{}".format(str(n) + str(i)))
        elif(i > n):
            print("{}".format(str(n) + str(i)) + ", ", end="")
