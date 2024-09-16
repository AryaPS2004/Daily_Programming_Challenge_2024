"""
Problem : Trapping Rain Water
You are given an array height[] of non-negative integers where each element represents the height of a bar in a histogram-like structure. These bars are placed next to each other, and the width of each bar is 1 unit. When it rains, water gets trapped between the bars if there are taller bars on both the left and right of the shorter bars. The task is to calculate how much water can be trapped between these bars after the rain.

Input :
An integer array height[] where each element represents the height of a bar in the histogram.
Example : 
height[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Output :
* An integer representing the total units of water that can be trapped between the bars.
Example
Output: 6
"""


def trap(height):
    if not height:
        return 0
    
    l,r=0,len(height)-1
    leftMax,rightMax=height[l],height[r]
    res=0
    
    while l<r:
        if leftMax<rightMax:
            l+=1
            leftMax=max(leftMax,height[l])
            res+=leftMax-height[l]
        else:
            r-=1
            rightMax=max(rightMax,height[r])
            res+=rightMax-height[r]
            
    return res

height = list(map(int, input("Enter the heights of bars: ").split()))
print(f"Total water trapped: {trap(height)}")
