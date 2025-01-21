"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""


def longestCommonPrefix (strs: List[str]) -> str:
    result = ""

    for character in a[0]:
        result += character
    
        for word in a:
            if not word.startswith(result):
                result = result[:-1]

    return result


def longestCommonPrefixAnother(strs: List[str]) -> str:
    ans:str=""
    strs:list[str]=sorted(strs)
    first:str=strs[0]
    last:str=strs[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans 



if __name__ == "__main__":
    print(f"Longest prefix in ['flower', 'flow','flight']: {longestCommonPrefix(['flower', 'flow','flight'])}")
    print(f"Longest prefix in ['dog', 'racecar','car']: {longestCommonPrefix(['dog', 'racecar','car'])}")