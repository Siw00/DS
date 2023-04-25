#1. check wether given year is leap year or not
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")  
# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
CheckLeap(Year)  

#2. Program to arrange numbers in ascending order
limit= int(input("enter number of values to insert:"))
values=[]
for i in range(limit):
    num=int(input("enter value:"))
    values.append(num)
values= sorted(values)
print('the sorted values are',values)

#3. Find prime numbers in a given range
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

#4. program to convert celsius to farenheit and farenheit to celsius 
def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

def main():
    print("1. Convert celsius to farenheit")
    print("2. Convert farenheit to celsius")
    choice = input("Enter your choice: ")
    if choice == '1':
        celsius = float(input("Enter temperature in celsius: "))
        print(celsius_to_farenheit(celsius))
    elif choice == '2':
        farenheit = float(input("Enter temperature in farenheit: "))
        print(farenheit_to_celsius(farenheit))
    else:
        print("Invalid choice")

main()

#5. program to check if given string is palindrome
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

string = input("Enter a string: ")
if is_palindrome(string):
    print("String is palindrome")
else:
    print("String is not palindrome")
    
#6. Find GCD of two numbers
import math

a = int(input("enter first num:"))
b = int(input("enter second num:"))

print("the gcd of the numbers are:", math.gcd(a,b))

#7. program to perform sorting functions using numpy arrays
import numpy as np
arr = np.array([[14,23,3,44,15],[64,72,8,19,10]])
#arr= np.array(input("Enter the array: "))

# display choices
print("1. Sort row wise")
print("2. Sort column wise")
print("3. Sort whole array")
print("4. Sort into index of array")

# take choice from user
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Sorting row wise")
    print(np.sort(arr, axis=0))
elif choice == 2:
    print("Sorting column wise")
    print(np.sort(arr, axis=1))
elif choice == 3:
    print("Sorting whole array")
    print(np.sort(arr))
elif choice == 4:
    print("Sorting into index of array")
    print(np.argsort(arr))

#8. program to compute product of elements in a list
def product(list):
    prod = 1
    for i in list:
        prod = prod * i
    return prod
#input list
list=int(input("Enter the list of numbers:"))
print("Product of elements in the list is :", product(list))

#9.Export one pandas dataframe to csv
import pandas as pd
# in df add name age and designation sample data
df = pd.DataFrame({'name': ['John', 'Peter', 'Paul', 'Mary'],
                     'age': [32, 43, 28, 33],
                        'designation': ['Manager', 'VP', 'CEO', 'CFO']})

df.to_csv('foo.csv', index=False)

print("the csv file is created successfully to the file named foo.csv")

#10. check wether given key is present in a dictionary 
dict = eval(input("Enter dictionary: "))
# take user input for keys
key = eval(input("Enter key to check: "))

for i in dict.keys():
    if i == key:
        print("Key is present in the dictionary")
        break
else:
    print("Key is not present in the dictionary")


#11.Write a NumPy program to create a one-dimensional array of single, two and three-digit numbers.
import numpy as np

print("One-dimensional array of single digit numbers:")
print(np.arange(1,10))

print("One-dimensional array of two digit numbers:")
print(np.arange(10,21))

print("One-dimensional array of three digit numbers:")
print(np.arange(100,111))

#12. Write a program to calculate the inverse of a square matrix
from scipy import linalg
import numpy as np

# Define a square matrix
sqr_matrix=np.array([[1,2],[4,5]])
# pass the matrix to the inv function
inv_matrix=linalg.inv(sqr_matrix)
print(inv_matrix)
