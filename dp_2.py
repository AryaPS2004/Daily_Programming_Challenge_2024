"""
Problem: Find the missing number
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input :
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output :
Return the missing integer from the array.
Example: Missing Number : 3
"""

def missing_num(arr,n):
    total_sum=n*(n+1)/2
    array_sum=sum(arr)
    return total_sum - array_sum

n = int(input("Enter the value of n: "))
arr = list(map(int, input(f"Enter elements: ").split()))
missing_number = missing_num(arr, n)
print(f"Missing Number: {missing_number}")
