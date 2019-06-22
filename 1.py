print ("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

###
'''
Printing Version for Python 
'''
import sys
print( "Python Version")
print(sys.version)
print("Version Info.")
print(sys.version_info)

###3

import datetime as dt
now = dt.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
 
###4
###Radius of a circle as input and computes area
from math import pi
r = float(input("Input the radius:"))
area =  (pi * r**2)
print("Area of the Circle" + " of radious " + str(r) + " is " + str(area) )

###5
### Name in Reverse order
f = str(input("Plese input your first name:"))
l = str(input("Please input your second name:"))
print(l + " " + f)