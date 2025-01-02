'''You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m = 0
        n = len(matrix[0]) - 1
        while m < len(matrix):
            if target >= matrix[m][n]:
                if target == matrix[m][n]:
                    return True
                else:
                    m += 1
            else : 
                left = 0
                right = n
                while left <= right:
                    mid = (left + right) // 2
                    if target == matrix[m][mid]:
                        return True
                    if target > matrix[m][mid]:
                        left = mid + 1
                    if target < matrix[m][mid]:
                        right = mid - 1
                return False
        return False