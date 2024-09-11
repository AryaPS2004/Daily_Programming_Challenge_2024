def find_dup(arr):
    slow=arr[0]
    fast=arr[0]
    
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if slow==fast:
            break
        
    slow=arr[0]    
    while slow!=fast:
        slow=arr[slow]
        fast=arr[fast]
        
    return fast

arr = list(map(int, input("Enter the array elements: ").split()))
duplicate_number = find_dup(arr)
print(f"Duplicate Number: {duplicate_number}")