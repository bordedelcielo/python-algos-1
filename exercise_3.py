# Write a program to implement a Linear Search Algorithm. 
# Also in a comment, write the Time Complexity of the following algorithm.
# Hint: Linear searching will require searching a list for a given number 
# Binary search on geeks for geeks may help.

nums_list = [10,23,45,70,11,15]
target = 70


# example below pulled from # https://www.tutorialspoint.com/linear-search-in-python-program
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i

arr = nums_list
x = target

# arr = ['t','u','t','o','r','i','a','l']
# x = 'a'
print("element found at index "+str(linearsearch(arr,x)))