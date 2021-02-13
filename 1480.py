def test(nums):
    ans = []
    for i in nums:
        if ans == []:
            ans.append(i)
        else:
            ans.append(i + ans[-1])
    return ans

print(test([2,3,0,2]))

# 28 ms runtime, 14.4 MB memory