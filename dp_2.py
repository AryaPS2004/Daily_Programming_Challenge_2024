def missing_num(arr,n):
    total_sum=n*(n+1)/2
    array_sum=sum(arr)
    return total_sum - array_sum

n = int(input("Enter the value of n: "))
arr = list(map(int, input(f"Enter elements: ").split()))
missing_number = missing_num(arr, n)
print(f"Missing Number: {missing_number}")
