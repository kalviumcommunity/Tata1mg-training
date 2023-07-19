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

# Question 11 Geeks for geeks
# Question Link:https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# Answer 
def merge(self,arr1,arr2,n,m):
        #code here
        for i in range(m):
            arr1.append(arr2[i])
            arr2[i]=''
        arr1.sort()

# Question 12 Geeks for geeks
# Question Link: https://practice.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1
# Answer 
def __init__(self, n=100):
        self.arr = [[], []]

    def push1(self, x):
        self.arr[0].append(x)
        
    def push2(self, x):
        self.arr[1].append(x)

    def pop1(self):
        if self.arr[0]:
            return self.arr[0].pop()
        return -1

    def pop2(self):
        if self.arr[1]:
            return self.arr[1].pop()
        return -1

# Question 13 leetcode
# Question Link: https://leetcode.com/problems/ugly-number/description/
# Answer 
def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n=n//i
        return n==1


# Question 14 Geeks for Geeks
# Question Link:https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1
# Answer
def deleteMid(self, s, sizeOfStack):
        # code here
        i=(sizeOfStack-1)//2
        s.pop(i)
        return s

# Question 15 leetcode
# Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
# Answer
def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in  range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left

# Question 16 leetcode
# Question Link: https://leetcode.com/problems/merge-sorted-array/submissions/
# Answer
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,n+m):
            nums1[i]=nums2[i-m]
        nums1.sort()

# Question 17 Geeks for Geeks
# Question Link: https://practice.geeksforgeeks.org/problems/queue-reversal/1
# Answer
def rev(self, q):
        #add code here
        stack=[]
        while not q.empty():
            stack.append(q.get())
        while len(stack)!=0:
            q.put(stack.pop())
        return q

# Question 18 Geeks for Geeks
# Question Link: https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1
# Answer
def FirstNonRepeating(self, A):
		# Code here
        count={}
		sequence=[]
		result=""
		
		for ch in A:
		    count[ch] = count.get(ch, 0) + 1
		
		    if count[ch]==1:
		        sequence.append(ch)
		    elif count[ch]==2:
		        if ch in sequence:
		            sequence.remove(ch)
		    
		    if sequence:
		        result += sequence[0]
		    else:
		        result += '#'
		        
		return result

# Question 19 Geeks for Geeks
# Question Link:https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
# Answer
def LongestRepeatingSubsequence(self, str):
		# Code here
		n = len(str)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
 
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
 
        return dp[n][n]

# Question 20 Leetcode
# Question Link: https://leetcode.com/problems/length-of-last-word/submissions/
# Answer
def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        ans = 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        return ans

# Question 21 Leetcode
# Question Link: https://leetcode.com/problems/number-of-1-bits
# Answer
def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n%2
            n = n >> 1
        return ans

# Question 22 Geeks for Geeks
# Question Link: https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1
# Answer
def longestPalinSubseq(self, S):
        # code here
        n = len(S)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for cl in range(2, n+1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if S[i] == S[j] and cl == 2:
                    dp[i][j] = 2
                elif S[i] == S[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]

# Question 23 Leetcode
# Question Link:https://leetcode.com/problems/remove-element/submissions/
# Answer
def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Question 24 Leetcode
# Question Link:https://leetcode.com/problems/palindrome-number/submissions/
# Answer
def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        reversedNum = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversedNum = reversedNum * 10 + digit
            temp //= 10

        return reversedNum == x