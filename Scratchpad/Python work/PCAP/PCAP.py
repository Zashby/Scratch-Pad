"""Just labs I had to complete during PCAP, felt like a waste to delete them afterwards"""
def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year%100==0:
        return year%400==0
    else:
        return year%4==0
        
def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    if month<=7 and month%2!=0:
        return 31
    elif month ==2:
        return 28 + int(is_year_leap(year))
    elif month >7 and month%2 ==0:
        return 31
    else:
        return 30
        

def day_of_year(year, month, day):
#
# Write your new code here.
#
    yearDay=0
    for x in range(1,month):
        yearDay+=(days_in_month(year, x))
        print(yearDay)
    return yearDay+day

print(day_of_year(2000, 12, 31))

def liters_100km_to_miles_gallon(liters):
#
# Write your code here.
#
    gallons=liters/3.785411784
    miles=(100_000/1609.344)
    return miles/gallons
    
    return liters

def miles_gallon_to_liters_100km(miles):
#
# Write your code here
#
    
    km=miles*1609.344
    liters = 100000/(km/3.785411784)
    return liters


from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(exp(2 * log(2)))
print(log(e, e) == exp(0))

from platform import platform, machine, processor, system, version
print(platform())
print(platform(1))
print(platform(0,1))

print(machine())


print(processor())

print(system())

print(version())    

from PCAP_module import suml, prodl



zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import sys

for p in sys.path:
    print(p)

import pandas

print(version()) 

def mysplit(strng):
    """Emulates strip function. Probably could clean up but first draft works for required instructions:
    Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

    it should accept exactly one argument - a string;
    it should return a list of words created from the string, divided in the places where the string contains whitespaces;
    if the string is empty, the function should return an empty list;
    its name should be mysplit()
    """
    end_list=[]
    check=0
    strng = strng.strip()
    
    if strng:
        for i, ch in enumerate(strng):
            if ch == " ":
                end_list.append(strng[check:i].strip())
                check=i
        end_list.append(strng[check:len(strng)].strip())
    return end_list
        

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
