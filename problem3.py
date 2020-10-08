#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""
def factors(a):
    List=[a]
    for i in range (1,a):
        if a%i==0:
            List.append(i)
        List.sort()
    return List

x=factors(12)
print(x)

y=factors(37)
print(y)
