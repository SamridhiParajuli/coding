"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from collections import deque

class Stack:
    def __init__(self)->None:
        self.collection = deque()

    def push(self, value)->None:
        self.collection.append(value)

    def pop(self):
        return self.collection.pop()
    
    def is_empty(self)->bool:
        return len(self.collection)==0
    
    def size(self)->int:
        return len(self.collection)



def valid_parantheses(s:str)->bool:
    st:Stack = Stack()
    p_map:dict[str:str] = {"]":"[", ")":"(", "}":"{"}
    for el in s:
        if el in p_map.values():
            st.push(el)
        else:
            if (not st.is_empty()) and (st.collection[-1] == p_map[el]):
                st.pop()
            else:
                return False
    return not st.size()


if __name__ == "__main__":
    print(f"Is (()) valid? {valid_parantheses('(())')}")
    print(f"Is (() valid? {valid_parantheses('(()')}")
    print(f"Is ([]) valid? {valid_parantheses('([])')}")
    print(f"Is ([)] valid? {valid_parantheses('([)]')}")