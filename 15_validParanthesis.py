'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
'''
class Solution(object):
    def isValid(self, s):
        hashmap = {')' : '(', ']' : '[', '}' :'{'}
        stack = []
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0