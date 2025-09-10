from math import gcd
from typing import List

def gcdOfString(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return "None"
    g = gcd(len(str1), len(str2))
    return str1[:g]

def getConcatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2*n)
    for i in range(2*n):
        ans[i] = nums[i % n]
    return ans


    
    
print(gcdOfString("ABCDABCD", "ABCD"))
print(gcdOfString("ABABABAB", "AB"))
print(gcdOfString("ABBAABBAABBA", "DDF"))
print(getConcatenation([1,2,1]))
print(getConcatenation([1,3,2,1]))
