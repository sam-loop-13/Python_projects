#!/usr/bin/python3
#print("Hello")
def s_ar(array):
    sum = 0
    for element in array:
        sum = sum + element
    return sum

ar2 = [3,4,6,4,3,2,2,4,-6,-3,-6]  
ar3 = [3,6,7,9,66,85,2,1]
print(s_ar(ar2),s_ar(ar3))

"""

array1 = [2, 888, 44,5,677,34,0,-3,30]
sum=0
min = array1[0]
max = min
for x in array1:
    sum = sum + x
    if x < min:
        min = x
    if x > max:
        max = x 
print(sum, min, max)            



"" sum = (sum + x)
print ("Sum =",(sum)) 

min = array1[0]
for a in array1:
    if a <= 0:
        min = a
        print (min)
#print ("min = ",min)

max = array1[0]
for a in array1:
    if a > max:
        max = a
print (max)        

for q in array1:
    if q % 2 != 0 and q != 0: 
        print (q)
people = [
        {
            "Name": "Bob",
            "Age": 55,
        },
        {
            "Name": "Alice",
            "Age": 44
        },
        {
            "Name": "Phill",
            "Age": 14
        },
        {
            "Name": "Den",
            "Age": 26
        }

]
Names = []

def my_f(name):
    print(name,"To young!") 

#print (people)
for x in people:
    if x["Age"] >= 20:
        Names.append(x["Name"])
    else:
        my_f(x["Name"])
           
print(Names)

my_f("Hello")

"""

