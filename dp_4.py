"""
Problem : Merge Two Sorted Arrays
You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input :
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
"""

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
