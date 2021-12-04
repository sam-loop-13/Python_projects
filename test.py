a = input('enter 1st ->')
b = input('enter 2nd ->')
x = input('action ')

if x == '+':
    c = int(a)+int(b)
    print( a +" + "+ b +" = " +str(c))

elif x == '-':
    c = int(a)-int(b)
    print( a +" - "+ b +" = " +str(c))    

elif x == '*':
    c = int(a)*int(b)
    print( a +" * "+ b +" = " +str(c))    

elif x == '/':
    c = int(a)/int(b)
    print( a +" / "+ b +" = " +str(c))     

else :
    print('wrong action !')    
    
