'''
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
'''
class Solution(object):
    def maxArea(self, height):
        res = 0
        l , r = 0, len(height) -1
        while l < r:
            res = max(res,(r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else :
                r -= 1
        return res