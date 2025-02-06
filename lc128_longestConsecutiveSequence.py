from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n in nums:
            if (n-1) not in count:
                # n is good start
                length = 0
                while n in count:
                    length += count[n]
                    n += 1
                maxLength = max(maxLength, length)
        return maxLength


if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    s = Solution()
    result = s.longestConsecutive(nums)
    print("output: " + str(result))