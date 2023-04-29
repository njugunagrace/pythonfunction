from statistics import mean


def add(a,b):
    answer = a+b
    return answer

def subtract(a,b):
    answer = a-b
    return answer  

def divide(a,b):
    answer = a/b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def remainder(a,b):
    answer = a%b
    return answer


def dict():
    answer = {"a":4,"b":9,"c":10,"d":6}  
    count = 0
    for number in answer:
        if int(number) in answer and int(number) >= 10 in answer:
            count += 1

            return count
 
    return answer


# Write a Python program to count the number of items in a dictionary that have a value greater than a certain number.

# my_dict= {"a":6,"b":9,"c":7,"d":10,"e":9}
# values =7
# count = 0
# for key,value  in my_dict.items():
#     if value > values:
#      count += 1
# print(count)

# Write a function that takes a list of numbers as input and returns a new list with all duplicate numbers removed.
def numbers(num):
    return list(set(num))
my_numbs= [30,45,34,34,28,30]
print(numbers(my_numbs))

# Write a function that takes a string as input and returns the length of the string.
def getlength(string):
    return len(string)
word = "Grace"   
print (getlength(word))

# Write a function that takes a list of numbers as input and returns the average of the numbers.
# def numbs(num):
#     nums = [3,4,5,6]
# numerals= numbs.average(nums)
# print (numerals)




