# Exercise 1
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

import calendar
i=int(input("enter the month:"))
print(f'month {i} is{calendar.month_name[i]}')

 # Exercise 2
# A certain cinema currently sells tickets for a full price of 6 pounds,but always sells tickets for half price to people who are less than 16 years
# old,and for a third of the price for people who are 60 years old or more.

age = int(input("Enter your age: "))
if age < 16:
    print("Your ticket costs £3.00")
elif age < 60:
    print("Your ticket costs £6.00")
else:
    print("Your ticket costs £2.00")

# Exercise 3
"""Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a
healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
BMI= weight(kg)/height2(m2)
BMI Weight Status Categories table
BMI range- kg/m2 Category
Below 18.5 Underweight
18.5 -24.9 Normal
25 - 29.9 Overweight
30 & Above Obese"""

weight=float(input("enter weight in kg:"))
height=float(input("enter height in m:"))
bmi=weight/(height*height)

print('BMI is:',bmi)

if bmi<18.5:
    print(' you are under weight')
elif 18.5<=bmi<25:
    print(' you are normal')
elif 25<=bmi<30:
    print('you are overweight')
else:
    print('you are obese')


# Exercise 4
# Write a Python program to receive 3 numbers from the user and print the greatest among them.
n1=int(input('enter the number 1:'))
n2=int(input('enter the number 2:'))
n3=int(input('enter the number 3:'))

if n1>n2 and n1>n3:
    largest=n1
elif n2>n1 and n2>n3:
    largest=n2
else:
    largest=n3

print(f'largest among {n1},{n2}and {n3} is {largest}')


# Exercise 5
# Find the factorial of a given number using loops
num=int(input('enter a number :'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print('factorial of',num, 'is',fact)
# Exercise 6
# Reverse a number using while loop
i=int(inpuut is ',rev)
Exercise 7
Finding the multiples of a number using loop
n=int(input('enter the number:'))
print('multiples of ',n,)
i=0
for i in range(1,11):
    print(n*i)
# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
for i in range(1,11):
    if i==6:
        break
    else:
        print(i)
# Exercise 9
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
i=0
for i in range (1,11):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    elif i%5==0 and i%3==0:
        print('fizzbuzz')
    else:
        print(i)
# Exercise 10
# Write a program to print the following pattern:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
n=5

for i in range(n):
    for j in range(n-i-1,-1,-1):
        print(j+1,end=' ')
    print()