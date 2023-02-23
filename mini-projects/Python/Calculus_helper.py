import math

# Serves as a quick helper for simple math things I have to do repeatedly for class.

def radio_decay(start, rate, time ):
    """Applies radioactive decay rate function to input parameters. Only determines remaining mass, cannot reverse currently"""
    remainder = start*math.e**(-rate*time)
    return remainder

print('Hello! Please input the following information to determine the remaining mass following radioactive decay!')
start = float(input('Please input the starting mass as a number (g): '))
rate = float(input('Please input the decay rate as a (positive) number: '))
time = float(input('Please input the time elapsed as a number: '))

print('You are left with ', radio_decay(start,rate,time), "g")