'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
class Solution(object):
    def isPalindrome(self, s):
        palindrome = []
        for c in s:
            if c.isalnum():
                palindrome.append(c.lower())
        return palindrome == palindrome[::-1]

# class Solution(object):
#     def isPalindrome(self, s):
#         res = ""
#         if len(s) == 0:
#             return True
#         s = s.lower()
#         for a in s:
#             if a.isalpha() or a.isdigit():
#                 res += a
#         left = 0
#         right = len(res) - 1
#         while left <= right:
#             if res[left] != res[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
