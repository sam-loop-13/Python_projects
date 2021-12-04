#!/usr/bin/python3

from colorama import Fore, Back, Style

#
print(Back.GREEN)
print(Fore.BLACK)
what = input('действия ?')

print(Back.GREEN)
print(Fore.BLACK)

a = float (input("1-е чистло : "))
b = float (input("2-е чистло : "))

if what == "+":
    c = a + b
    print("cсумма : " + str(c))
elif what == "-":
    c = a - b
    print("разница : " + str(c)) 
