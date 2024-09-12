def merge_arrays(nums1, nums2, m, n):
    last = m + n - 1  
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


def take_input():
    
    nums1 = list(map(int, input("Enter the elements of nums1: ").split()))
    nums2 = list(map(int, input("Enter the elements of nums2: ").split()))

    m = int(input("Enter the number of valid elements in nums1: "))
    n = int(input("Enter the number of elements in nums2: "))

    nums1 += [0] * n


    merge_arrays(nums1, nums2, m, n)

    print("After merging:")
    print("Merged nums1:", nums1)


take_input()
