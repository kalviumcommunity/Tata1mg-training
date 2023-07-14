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

# Question 7 Geeks for geeks
# Question Link:https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1
# Answer
 def power(self,N,R):
        #Your code here
        mod = int(1e9) + 7 
        return pow(N, R, mod)

# Question 8 Geeks for geeks
# Question Link: https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1
# Answer
def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        left=0
        prod=1
        count=0
        for i in range(n):
            prod*=a[i]
            while prod>=k and left<=i:
                prod/=a[left]
                left+=1
            count+=i-left+1
        
        return count

# Question 9 Geeks for geeks
# Question Link:https://practice.geeksforgeeks.org/problems/copy-set-bits-in-range0623/1
# Answer
def setSetBit(self, x, y, l, r):
        # code here
        mask = (1<<(r - l + 1))
        mask-=1 
        mask = (mask <<(l - 1))
        mask = mask & y
        x = x | mask
        return x

# Question 10 Geeks for geeks
# Question Link: https://practice.geeksforgeeks.org/problems/unique-frequencies-of-not/1
# Answer 
def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        a=[]
        b=[]
        for i in arr:
            if i in a:
                pass
            else:
                c=arr.count(i)
                if c in b:
                    return False
                else:
                    b.append(c)
                    a.append(i)
        return True

# Question 10 Geeks for geeks
# Question Link:https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# Answer 
def merge(self,arr1,arr2,n,m):
        #code here
        for i in range(m):
            arr1.append(arr2[i])
            arr2[i]=''
        arr1.sort()
