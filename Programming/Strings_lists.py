#PreCondition: a, b, c, d are positive integers <= length of string 
#PostCondition: The string between a,b c,d

String = raw_input('Enter String: ')
a = raw_input('a: ')
b = raw_input('b: ')
c = raw_input('c: ')
d = raw_input('d: ')

def slicer():
    return String[a:(b + 1)] + String[c:(d + 1)]
    
print slicer()
