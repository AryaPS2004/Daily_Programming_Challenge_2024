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