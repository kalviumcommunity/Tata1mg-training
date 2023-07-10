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
        return False

# Question 3 Leetcode
# Question Link: https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1
# Answer
def findTriplets(self, arr, n):
        #code here
        found = False
        arr.sort()
        for i in range(n - 1):
            l = i + 1
            r = n - 1
            x = arr[i]
            while l < r:
                if x + arr[l] + arr[r] == 0:
                    l += 1
                    r -= 1
                    found = True
                    break
                elif x + arr[l] + arr[r] < 0:
                    l += 1
                else:
                    r -= 1
            if found:
                break
        return found

# Question 4 Leetcode
# Question Link: https://practice.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1
# Answer
for i in range(n):
            for j in range(i+1 ,n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j] 
