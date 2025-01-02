'''
 GROUP ANAGRAM : Given an array of strings strs, group the anagrams together.
 Iterate over the array and sort the word for key and add word as list into the hashmap 
 if an already key is present, append it to the value of the key and return the list of the answer.
'''

from collections import defaultdict
anagram = defaultdict(list)
strs = ["eat","tea","tan","ate","nat","bat"]
for word in strs:
    count = [0] * 26
    for char in word:
        count[ord(char) - ord('a')] += 1
    anagram[tuple(count)].append(word)

print(list(anagram.values()))