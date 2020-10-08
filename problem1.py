#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse (a,b,boolean):
    if boolean is False:
        answer=int(math.sqrt(float(a)**2+float(b)**2))
    if boolean is True:
        if a>b:
            answer=int(math.sqrt(float(a)**2-float(b)**2))
        if a<b:
            answer=int(math.sqrt(float(b)**2-float(a)**2))
    return answer

x=hypotenuse(3,4,False)
print(x)

y=hypotenuse(13,5,True)
print(y)
