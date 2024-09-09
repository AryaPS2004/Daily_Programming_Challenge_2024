def sorts(arr):
    low,mid=0,0
    high=len(arr)-1
    
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
            
        elif arr[mid]==1:
            mid=mid+1
            
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high=high-1
    return arr

arr = list(map(int, input("Enter the array elements: ").split()))
sorted_arr = sorts(arr)
print("Sorted array:", sorted_arr)