# """Just labs I had to complete during PCAP, felt like a waste to delete them afterwards"""

import math

from string import ascii_lowercase, ascii_uppercase, ascii_letters

from calendar import Calendar

# def is_year_leap(year):
# #
# # Your code from LAB 4.3.1.6.
# #
#     if year%100==0:
#         return year%400==0
#     else:
#         return year%4==0

# def days_in_month(year, month):
# #
# # Your code from LAB 4.3.1.7.
# #
#     if month<=7 and month%2!=0:
#         return 31
#     elif month ==2:
#         return 28 + int(is_year_leap(year))
#     elif month >7 and month%2 ==0:
#         return 31
#     else:
#         return 30


# def day_of_year(year, month, day):
# #
# # Write your new code here.
# #
#     yearDay=0
#     for x in range(1,month):
#         yearDay+=(days_in_month(year, x))
#         print(yearDay)
#     return yearDay+day

# print(day_of_year(2000, 12, 31))

# def liters_100km_to_miles_gallon(liters):
# #
# # Write your code here.
# #
#     gallons=liters/3.785411784
#     miles=(100_000/1609.344)
#     return miles/gallons

#     return liters

# def miles_gallon_to_liters_100km(miles):
# #
# # Write your code here
# #

#     km=miles*1609.344
#     liters = 100000/(km/3.785411784)
#     return liters


# from math import e, exp, log

# print(pow(e, 1) == exp(log(e)))
# print(exp(2 * log(2)))
# print(log(e, e) == exp(0))

# from platform import platform, machine, processor, system, version
# print(platform())
# print(platform(1))
# print(platform(0,1))

# print(machine())


# print(processor())

# print(system())

# print(version())

# from PCAP_module import suml, prodl


# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))

# import sys

# for p in sys.path:
#     print(p)


# print(version())

# def mysplit(strng):
#     """Emulates strip function. Probably could clean up but first draft works for required instructions:
#     Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

#     it should accept exactly one argument - a string;
#     it should return a list of words created from the string, divided in the places where the string contains whitespaces;
#     if the string is empty, the function should return an empty list;
#     its name should be mysplit()
#     """
#     end_list=[]
#     check=0
#     strng = strng.strip()

#     if strng:
#         for i, ch in enumerate(strng):
#             if ch == " ":
#                 end_list.append(strng[check:i].strip())
#                 check=i
#         end_list.append(strng[check:len(strng)].strip())
#     return end_list


# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

# def ledNum(nums):
#     """Prints LED version of input integer numbers. I am too lazy to finish building the dictionary."""
#     nums=str(nums)
#     L = "#"
#     led = {
#         "1":[[' ',L],[' ',L],[' ',L],[' ',L],[' ',L]],
#         "2":[[L,L,L],[' ',' ',L],[L,L,L],[L,' ',' '],[L,L,L]]
#     }
#     for x in range(5):
#         for num in nums:
#             print(''.join(led[num][x]),end=" ")
#         print("")


# ledNum(21212122)


# def advancedROT():
#     shifted_text = ''
#     shift=0
#     text = input("Please enter the text you would like to encrypt: ")
#     while not shift:
#         try:
#             shift = int(input('Please enter a rotation value from 1 to 25: '))
#         except:
#             print("incorrect value, please try again.")
#         if shift > 25 or shift <= 0:
#             shift=0
#             print('Try again')
#     for letter in text:
#         if letter in ascii_lowercase:
#             shifted_text += ascii_lowercase[(ascii_lowercase.find(letter)+shift)%26]
#         elif letter in ascii_uppercase:
#             shifted_text += ascii_uppercase[(ascii_uppercase.find(letter)+shift)%26]
#         else:
#             shifted_text += letter

#     return shifted_text


# print(advancedROT())

# def recurveAdd(date):
#     sum=0
#     for x in date:
#         sum += int(x)
#     return str(sum)


# def digitOfLife():
#     date=""
#     numdate=0

#     while not numdate:
#         try:
#             date=input("Please enter your date as numbers formatted as YYYYMMDD: ")
#             numdate = int(date)
#         except:
#             print('That is an incorrect format, please try again.')
#             continue
#         if len(date) < 8:
#             numdate=0
#             print("I need the whole date please. Try again.")

#     while len(date) >1 :
#         date = recurveAdd(date)
#     return date


# print(digitOfLife())

# def stringFinder(word, string):
#     word=word.lower()
#     string=string.lower()

#     check = sum([1 for x in word if x in string])
#     if len(word) == check:
#         return "Yes"
#     else:
#         return "No"


# print(stringFinder('donor',
# 'Nabucodonosor'))


# print(stringFinder('donut',
# 'Nabucodonosor'))

# def sudokuCheck(sudoku):
#     """ Takes a massive integer (81 digits) and returns if it is a winning sudoku game"""
#     check=[]
#     sudoku_list=[]
#     sudoku=list(str(sudoku))
#     # Array build
#     for x in range(9):
#         sudoku_list.append([sudoku[x] for x in range(9)])
#         if len(set(sudoku_list[x])) == 9:
#             del sudoku[0:9]
#         else:
#             return "no"
#     # vertical
#     for x in range(9):
#         if len(set([sudoku_list[y][x] for y in range(9)])) == 9:
#             pass
#         else:
#             return "No"

#     for y in range(0,7, 3):
#         for x in range(9):
#             first, second, third = sudoku_list[x][y:y+3]
#             check+= first, second, third
#             if len(check) == 9:
#                 if len(set(check))==9:
#                     check=[]
#                 else:
#                     return "No"
#     return "Yes"


# print(sudokuCheck(295743861431865927876192543387459216612387495549216738763524189928671354154938672))

# print(sudokuCheck(195743862431865927876192543387459216612387495549216738763524189928671354254938671))

# print(sudokuCheck(195741862431865927876192543387459216612387495549216738763524189928671354254938671))


# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         #
#         # Write code here
#         #
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def __str__(self):
#         #
#         # Write code here
#         #
#         return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


#     def next_second(self):
#         #
#         # Write code here
#         #
#         if self.seconds + 1 == 60:
#             self.seconds = 0
#             self.minutes += 1
#             if self.minutes == 60:
#                 self.minutes = 0
#                 self.hours += 1
#                 if self.hours == 24:
#                     self.hours = 0
#         else:
#             self.seconds += 1

#     def prev_second(self):
#         #
#         # Write code here
#         #
#         if self.seconds == 0:
#             self.seconds = 59
#             self.minutes -=1
#             if self.minutes < 0:
#                 self.minutes =59
#                 self.hours -=1
#                 if self.hours <0:
#                     self.hours = 23
#         else:
#             self.seconds -= 1


# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)


# class WeekDayError(Exception):
#     def __init__(self):
#         Exception.__init__(self)


# class Weeker:
#     #
#     # Write code here.
#     #
#     __days = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#     def __init__(self, day='Mon'):
#         #
#         # Write code here.
#         #
#         if day in self.__days:
#             self.__day = day
#         else:
#             raise WeekDayError

#     def __str__(self):
#         #
#         # Write code here.
#         #
#         return self.__day

#     def add_days(self, n):
#         #
#         # Write code here.
#         #

#         index = self.__days.index(self.__day)  + n
#         self.__day = self.__days[index%7]


#     def subtract_days(self, n):
#         #
#         # Write code here.
#         #

#         index = abs(self.__days.index(self.__day) - n)
#         self.__day = self.__days[-index%7]


# try:
#     weekday = Weeker('Mon')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Monday')
# except WeekDayError:
#     print("Sorry, I can't serve your request.")


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         #
#         # Write code here
#         #
#         return self.__x

#     def gety(self):
#         #
#         # Write code here
#         #
#         return self.__y

#     def distance_from_xy(self, x, y):
#         #
#         # Write code here
#         #
#         side_x = (x-self.getx())**2
#         side_y = (y - self.gety())**2
#         return math.sqrt(side_x+side_y)

#     def distance_from_point(self, point):
#         #
#         # Write code here
#         #
#         side_x = (point.getx()-self.getx())**2
#         side_y = (point.gety() - self.gety())**2
#         return math.sqrt(side_x+side_y)


# print(Point.__dict__)
# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         #
#         # Write code here
#         #
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         #
#         # Write code here
#         #
#         sum_perimeter = 0
#         for x in range(3):
#             sum_perimeter += self.__vertices[x].distance_from_point(
#                 self.__vertices[x-1])
#         return sum_perimeter


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())


# from string import ascii_letters, ascii_lowercase

# countDict = {x: 0 for x in ascii_lowercase}

# inputFile = input("Enter the file name: ")

# openFile = open(f"{inputFile}.txt", "r")

# for char in openFile.read():
#     if char in ascii_letters:
#         if char.lower() in countDict:
#             countDict[char.lower()] += 1

# openFile.close()

# # Change sort order

# sort_by_number = sorted(countDict.items(), key=lambda x: x[1], reverse=True)
# dict_by_number = dict(sort_by_number)

# for key, value in dict_by_number.items():
#     if value != 0:
#         print(f"{key} -> {value}")

# writeFile = open(f"{inputFile}.hist", "w")
# for key, value in dict_by_number.items():
#     if value != 0:
#         writeFile.write(f"{key} -> {value} \n")
# writeFile.close()

# class StudentsDataException(Exception):
#     def __init__(self):
#         Exception.__init__(self)


# class BadLine(StudentsDataException):
#     # Write your code here.
#     pass

# studentDict = {}
# studentFile = input("Enter Student data file name: ")

# try:
#     openFile = open(f"{studentFile}.txt", "r")
# except FileNotFoundError:
#     print("No file with this name located")

# for x in openFile.readlines():
#     student = x.split()
#     if len(student) != 3:
#         raise BadLine
#     name, grade = student[0] + " " + student[1], student[2]
#     try:
#         if name in studentDict.keys():
#             studentDict[name] += float(grade)
#         else:
#             studentDict[name] = float(grade)
#     except:
#         studentDict[name] = "Corrupted"

# for key, value in studentDict.items():
#     print(f"{key:20s} {value:1}")

# from calendar import Calendar


# class MyCalendar(Calendar):

#     def __init__(self):
#         Calendar.__init__(self)

#     def count_weekday_in_year(self, year, weekday):
#         self.setfirstweekday(weekday)
#         count = 0
#         for month in range(1, 13):
#             for data in self.monthdays2calendar(year, month):

#                 if data[0][0] != 0:
#                     count += 1

#         return count


# c = MyCalendar()

# print(c.count_weekday_in_year(2000, 6))
