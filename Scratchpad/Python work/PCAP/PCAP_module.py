#!/usr/bin/env python3 

__counter =0

if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")

def suml(lst):
    global __counter
    __counter +=1
    theSum = 0
    for element in lst:
        theSum += element
    return theSum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)