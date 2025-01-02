'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.
'''

class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

#         if not height:
#             return 0
#         maxi , mini = 0, 0
#         leftmax = [0] * len(height)
#         rightmax = [0]  * len(height)
#         res = 0
#         for i in range(len(height)):
#             maxi = max(maxi, height[i])
#             mini = max(mini, height[len(height)-1 - i])
#             leftmax[i] = maxi
#             rightmax[(len(height)-1) - i] = mini
        
#         for i in range(len(height)):
#             if min(leftmax[i], rightmax[i]) - height[i] >= 0:
#                 res += min(leftmax[i], rightmax[i]) - height[i]