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

# Question 4 Geeks for Geeks
# Question Link: https://practice.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1
# Answer
for i in range(n):
            for j in range(i+1 ,n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j] 

# Question 5 Geeks for geeks
# Question Link:https://practice.geeksforgeeks.org/problems/set-bits0143/1
# Answer
def setBits(self, N):
		# code here
        N=str(bin(N))
        return N.count('1')

# Question 6 Geeks for geeks
# Question Link: https://practice.geeksforgeeks.org/problems/find-nth-element-of-spiral-matrix/1
# Answer
def findK(self, a, n, m, k):
        # Write Your Code here
        ti = 0 
        bi = n
        fj = 0 
        bj = m 
        global_index = 0 
        while ti <= bi and fj <= bj :
            for j in range(fj , bj) :
                global_index += 1
                if global_index == k :
                    return a[ti][j]
            ti+=1
            for i in range(ti , bi):
                global_index += 1
                if global_index == k :
                    return a[i][bj-1]
            bj-=1
            for j in range(bj-1 , fj-1 ,  -1):
                global_index += 1
                if global_index == k :
                    return a[bi-1][j]
            bi-=1
            for i in range(bi-1 , ti-1 , -1):
                global_index += 1
                if global_index == k :
                    return a[i][fj]
            fj+=1
        return -1