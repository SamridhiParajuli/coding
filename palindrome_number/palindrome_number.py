"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


def palindrome_number(n:int)->bool:
    rev:int = 0
    temp:int = n
    while n>0:
        rev = (rev*10) + n%10
        n = n//10
    return temp==rev

if __name__ == "__main__":
    print(f"Is 121 palindromic? {palindrome_number(121)}")
    print(f"Is 1221 palindromic? {palindrome_number(1221)}")
    print(f"Is -1221 palindromic? {palindrome_number(-1221)}")
    print(f"Is 224 palindromic? {palindrome_number(224)}")