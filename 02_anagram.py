'''
Q2: ANAGRAM : An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

	Create two hashmaps and store the characters of the both strings and check whether they are equal or not. (efficient)
	 			Or
	Check whether the sorted of both strings are equal.
'''
def is_anagram(s, t):
    if len(s) != len(t):  
        return False
    
    freq = {}  
    for char in s:
        freq[char] = freq.get(char, 0) + 1  
    
    for char in t:
        if char not in freq or freq[char] == 0:  
            return False
        freq[char] -= 1  
    
    return True  

def is_anagram(s, t):
    return sorted(s) == sorted(t)  

