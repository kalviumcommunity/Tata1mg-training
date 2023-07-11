# Question 1 Geeks for Geeks
# Question Link: https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1
# Answer
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        arr.sort()
        a = m = 1
        for i in arr:
            if i > 0:
                if i == a:
                  m = a
                  a = a + 1
                elif i == m:
                    pass
                else:
                    break
        return a
# Question 2 Leetcode
# Question Link: https://leetcode.com/submissions/detail/987785100/
# Answer
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=len(s)
        y=len(t)
        if x!=y :
            return False

        sorted1=sorted(s)
        sorted2=sorted(t)

        if sorted1==sorted2:
            return True
