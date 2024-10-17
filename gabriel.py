# # def fibonacci(n):
# #     fib_sequence =[]

# #     a, b = 0,1
# #     for _ in range(n):
# #         fi
# # b_sequence.append(a)
    

# #     return fib_sequence

# # four glass
# # def four_glass(n):
# n =int(input("enter the number of rows"))
# for i in range(n):
#     print(''* i +'*'*(2 *(n-i)-1))
# for i in range(1,n-i):
#     print(''*(n-i) + '*'(2 * i-1))

# Example usage 
# #four_glass(n)

# # from sythenic import my_fun
# # i=6
# # k=9
# # my_fun(i,k)

# import csv
# import os

# # prompt the user for the CSV file name
# file_name=input("Enterthe name of the CSV file(with.csv extention):")

# # Check if the file exists
# file_exists= os. path.isfile(file_name)

# # Open the file in append mode('a'to append,newline="to handle a new lines correctly accross platforms)
# with open(file_name,mode='a', newline="" ) as file:
#  #Define the fieldname
#     fieldname=['name','age','gender']

# # Create a CSV Dictwriter object
# writer = csv.Dictwrite(file,fieldnames =fieldname)

# # If the file does not exist,write the header first
# if not file_exists:
#    writer.writeheader() 

# # Promptt the user for input 
# name = input("Nneamaka")
# age  = input("23")
# gender=input("female")


# #Write the input values to the CSV file 
# writer.writerow({'name: ' name,'age: 'age,'gender: ' gender})


# print(f" The data has been written to{file_name}.")


def addition (y,n):
  a = y+n
  return a

def substraction (g,q):
  w = g-q
  return w

def multiplication (s,h):
  d = s*h
  return d

def division(b,m):
  j = b/m
  return j


#create a dictionary map
operations = {'+': addition, '-': substraction , '*':multiplication, '/':division}


def calculator():
    num1= float (input('enter the first number: '))
    num2= float(input('enter the second number: '))
    operation=input(" enter an operation(+,-,*,/):")

    # Get the corresponding function from the dictionary and execute it
    if operation in operations:
        result = operations[operation](num1,num2)
        print(f"{num1}{operation}{num2} = {result}")
    else:
        print("Invalid operation")

# use get()to retrieve the function or none if not found
# result = operations.get(operation, lambda x,y:"Invalid operation")(num1,num2)

# print the result
# print(f"{num1}.{operation}.{num2}.={result}")")

# call the calculator function
calculator()