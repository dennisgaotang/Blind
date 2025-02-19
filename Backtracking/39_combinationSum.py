def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    res = []
    def helper(i, curArr, needSumTo):
        # some base case
        if needSumTo == 0:
            res.append(curArr.copy())
            return
        if needSumTo < 0:
            return
        if i >= len(nums):
            return
        # option 1: take this value
        curArr.append(nums[i])
        helper(i, curArr, needSumTo - nums[i])
        curArr.pop()

        # option 2: not take this value
        helper(i+1, curArr, needSumTo)

    helper(0, [], target)
    return res