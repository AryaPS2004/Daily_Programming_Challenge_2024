"""
Problem : Find the Leaders in an Array
You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

Input :
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output :
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]
"""

def find_leader(arr):
    n=len(arr)
    leaders=[]
    max_right=arr[-1]
    leaders.append(max_right)
    
    for i in range(n-2,-1,-1):
        if arr[i]>max_right:
            max_right=arr[i]
            leaders.append(max_right)
            
    leaders.reverse()
    return leaders

arr = list(map(int, input("Enter the array elements: ").split()))
print("Leaders:", find_leader(arr))
