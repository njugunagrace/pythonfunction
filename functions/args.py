def hello(*names):
    for name in names:
        print(f"Hello{name}")

def sum(*numbers): 
    answer=0
    for number in numbers:
        answer+=number
    return answer    
 
# write a function that accepts any no. of int and returns the result of multiply
#a function that can accept any number of positional args
def multiply(*nums):
    answer=1
    for num in nums:
        answer*=num           
    return answer    

#a fun that can accept any no. of keyword args
def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

# default arguments
def my_country(country="Kenya"):
    print(f"Hello from {country}")  

 
# Write a function that takes a list of numbers as input and returns the average of the numbers.
from statistics import mean
def number(*num):
    get_mean= mean(num)
    print(get_mean)   
# Write a function that takes a list of numbers as input and returns the maximum number in the list.
def numerals(*x):
    maxi = max(x) 
    print(maxi)
# Write a function that takes a list of strings as input and returns the longest string in the list.
def my_strings(*str): 
    return max(str,key=len)  
# a fun that removes duplicates
def remove_dups(*nums):
    empty=[]
    for num in nums:
        if num  not in empty:
            empty.append(num)
    print(empty)        
        
    #  to get the second largest number
def my_nums(*numb):
    sorted=numb.sort() 
    return sorted(-2)   

    
      
        