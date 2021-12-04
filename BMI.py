
w = int(input('Weight: '))
h = float(input('Height: '))
bmi = w/(h**2)
if bmi < 18.5:
    print('Underweight')
elif bmi >= 18.5 and bmi <25:
    print('Normal')
elif bmi >= 25 and bmi < 30:
    print('Overweight')
elif bmi >= 30:
    print('Obesity')
  
"""
while True:
    x=input('enter: ')
    if (x == '0'):
        break
print("sdsdsd")
print(85/(1.9**2))
"""