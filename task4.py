#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger (a):
    if float(a)%1==0:
        return True
    elif float(a)%1!=0:
        return False

x=isInteger(9.5)
print(x)

y=isInteger(-2)
print(y)
