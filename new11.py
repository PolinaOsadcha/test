# testing git
def dobutok (a,b):
    c = a+b 
    return c
d1 = dobutok(7,3)
d2 = dobutok(9,8)
print(d1)
print(d2)
d3 = dobutok(9,dobutok(1,0)) + dobutok(7,3)
print(d3)