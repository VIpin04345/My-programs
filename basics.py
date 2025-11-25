# 1.> write a program to add two numbers.

# (solution with predefine variables)
num1=30
num2= 40
sum=num1+num2
print('the sum of given number is',sum)


# (solution with user input)

num=float(input('enter a number '))
num2=float(input('enter another number'))
sum=num+num2
print('the sum of the provided to number is' , sum)
print('hello world')

# python program to find square root of a given number .


# (solution with exponentiation)

# num=81

num = int(input("enter a number:-"))
sr = num ** (1/2)  or (0.5)
print("the square root of the given number is ", sr)


# (solution using math module)

import math
num=int(input('enter a number :-'))
sr=math.sqrt(num)
print('the square root of the given number is',sr)


# write a program to find area of ractangle

height=float(input('enter the hight of trangle'))
width=float(input('enter the width of the trangle'))
area=(1/2)*height*width
print('the area of ractangle is ',area)


# write a program to find quadratic equation ax**2+bx+c=0
# whare, a ,  and c are the real numbers
# a!=0
import cmath
a=int(input('enter a number(a!=0):-'))
b=int(input('enter a number:-'))
c=int(input('enter a number:-'))
d=(b**2 )- (4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print('the roots are ',root1,root2)


# write a program to swap two variables.

var1=int(input('enter a number'))
var2=int(input('enter a number'))
print('before swapping',var1,var2)
temp=var1
var1=var2
var2=temp
print('after sapping',var1,var2)


# without using third variables

x=12
y=13
x,y=y,x
print(x,y)


# write a program to generate random number


import random
number=random.randint(1000,9999)
print(number)


# write a program to print from 1 to 10.

i = 1
while i <= 10:
    print(i)
    i += 1
print()

for i in range(1, 11):
    print(i)
print()

# write a program to print from 1 to n.

n = int(input("enter a number:-"))
i = 1
while i <= n:
    print(i)
    i += 1
print()


n = int(input("enter a number:-"))
for i in range(1, n + 1):
    print(i)
print()





i = 10
while i >= 1:
    print(i)
    i -= 1
print()

for i in range(10, 1 - 1, -1):
    print(i)
print()

# write a program to print from n to 1.


n = int(input("enter a number:-"))
i = 1
while n >= i:
    print(n)
    n -= 1
print()
n = int(input("enter a number:-"))
for i in range(n, 0, -1):
    print(i)

# write a program to print sum of n to 1.

n = int(input("enter a number:-"))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1
print(sum)


n = int(input("enter a number:-"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum = sum + i
print(sum)


n = int(input("enter your number:-"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)

# write a program to print sum of squre of 1 to n natural numbers.


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**2
    i += 1
print(sum)


n = int(input("enter a number:"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum += i**2
    i += 1
print(sum)

# write a program to print sum of cube of 1 to n natural numbers.


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**3
    i += 1
print(sum)

n = int(input("enter a number:"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum += i**3
    i += 1
print(sum)

# write a program to print only even number between 1 to n.


n = int(input("enter a number:-"))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


n = int(input("enter a number:-"))
i = 1
for i in range(i, n + 1):
    if i % 2 == 0:
        print(i)


# write a program to find sum of even number from 1 to n.

n = int(input("entera number:-"))
sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)


n = int(input("enter a number"))
sum = 0
i = 1
for i in range(i, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)


# write a program to find sum of first n even numbers.

n = int(input("enter  number :-"))
sum = 0
i = 1
while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i += 1
print(sum)
