"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def areanagrams(str1, str2):
    while True:
        if len(str1)!=len(str2):
            break
        elif sorted(str1)==sorted(str2):
            return True
        return False
print(areanagrams("anagram","nagaram"))
print(areanagrams("rat","car"))