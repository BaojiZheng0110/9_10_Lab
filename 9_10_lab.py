from math import gcd
from typing import List

def gcdOfString(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    g = gcd(len(str1), len(str2))
    return str1[:g]

def getConcatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2*n)
    for i in range(2*n):
        ans[i] = nums[i % n]
    return ans

if __name__ == "__main__":
    
    
    print("GCD of Strings")
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print ("Result:", gcdOfString(str1, str2))
    
    print("Concatenate Array")
    nums = input("Enter integers seperate by spaces: ")
    nums = list(map(int, nums.split()))
    print("Result:", getConcatenation(nums))
