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
    
#Solution to "Find Numbers with Even Number of Digits" problem
#Question Link "https://leetcode.com/problems/find-numbers-with-even-number-of-digits/"
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            count = 0
            k = i

            while k!= 0:
                k //= 10
                count += 1

            if count % 2 == 0:
                ans += 1

        return ans
    
#Solution to the "Reverse String" problem
#Question Link "https://leetcode.com/problems/reverse-string/"
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

#Solution to the "Best Time to Buy and Sell Stock" problem
#Question Link "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        ans = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                ans = max(ans, profit)
            else:
                left = right
            right += 1

        return ans
    
#Solution to the "Ugly Number" problem
#Question Link "https://leetcode.com/problems/ugly-number/"
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False

        for p in [2, 3, 5]:
            while n%p == 0:
                n = n // p
        return n == 1
    
#Solution to the "Length of Last Word" problem
#Question Link "https://leetcode.com/problems/length-of-last-word"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        ans = 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        return ans
    
#Solution to "Number of 1 Bits" problem
#Question link "https://leetcode.com/problems/number-of-1-bits"
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n%2
            n = n >> 1
        return ans
    
#Solution to "Remove Element" problem
#Question link "https://leetcode.com/problems/remove-element"
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
#Solution to "Remove Duplicates from Sorted Array" problem
#Question link "https://leetcode.com/problems/remove-duplicates-from-sorted-array"
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in  range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left

#Solution to "Palindrome Number" problem
#Question link "https://leetcode.com/problems/palindrome-number/"
class Solution:
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
    
#Solution to "Missing Number" problem
#Question Link "https://leetcode.com/problems/missing-number/""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(len(nums)):
            ans += (i - nums[i])
        return ans
    
#Solution to "Merge Sorted Array" problem
#Question link "https://leetcode.com/problems/merge-sorted-array/"
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in  range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()

#Solution to "Search Insert Position" problem
#Question link "https://leetcode.com/problems/search-insert-position/"
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        while begin <= end:
             bet = (begin + end) // 2
             if nums[bet] == target:
                 return bet
             elif nums[bet] < target:
                 begin = bet + 1
             else:
                 end = bet - 1
        return begin
    
#Solution to "Valid Palindrome" problem
#Question link "https://leetcode.com/problems/valid-palindrome/"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= ''
        for i in s:
            if i.isalnum():
                a += i.lower()
        i = 0
        j = len(a) - 1

        while i<j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True
            
#Solution to the "Two Sum" problem
#Question link "https://leetcode.com/problems/two-sum/"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j])