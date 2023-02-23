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


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))