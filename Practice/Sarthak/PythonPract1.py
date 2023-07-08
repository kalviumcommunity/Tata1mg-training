#This is the solution to the "Power of Two" problem in Leetcode which I earlier solved using C++
#Question link "https://leetcode.com/problems/power-of-two/"
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         for i in range(31):
            ans = 2 ** i
            if ans == n:
                return True
         return False
    

#Solution to the "Reverse Integer" question from Leetcode in Python
#Question link "https://leetcode.com/problems/reverse-integer/"
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        ans = 0
        while x!= 0:
            dig = x%10
            if ans > (2147483647 // 10) or ans < (-(2147483648) // 10):
                return 0

            ans = (ans*10) + dig
            x = x//10

        if is_negative:
            ans = -ans

        return ans
    
#Solution to "Truncate sentence" problem
#Question link "https://leetcode.com/problems/truncate-sentence/"
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space = 0
        i = 0
        n = len(s)
        re = ""
        
        while i != n:
            if s[i] == ' ':
                space += 1
                
            if space == k:
                break
            
            re += s[i]
            i += 1
        
        return re
    
#Solution to "Valid Anagram" problem
#Question link "https://leetcode.com/problems/valid-anagram/"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True

        return False