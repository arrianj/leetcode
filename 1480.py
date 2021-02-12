class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if ans == []:
                ans.append(i)
            else:
                ans.append(i + ans[-1])
        return ans

# 28 ms runtime, 14.4 MB memory