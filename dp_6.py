"""
Problem : Find All Subarrays with Zero Sum
You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.

Input :
An integer array arr of size n where n represents the number of elements in the array.
Example : 
Input: [1, 2, -3, 3, -1, 2]

Output :
- Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. The ending index (0-based) of the subarray.
- The output should list all subarrays that sum to zero. If no such subarrays are found, return an empty list.
"""


def find_subarray(arr):
    sum_map={}
    result=[]
    sum=0
    
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==0:
            result.append((0,i))
            
        if sum in sum_map:
            indices_list=sum_map[sum]
            for start in indices_list:
                result.append((start+1,i))
                
        if sum in sum_map:
            sum_map[sum].append(i)
        else:
            sum_map[sum]=[i]
            
    return result

arr = list(map(int, input("Enter the elements of the array: ").split()))
output = find_subarray(arr)
print("Subarrays with zero sum:", output)
