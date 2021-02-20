# Running Sum of 1d Array

def test(nums):
    ans = []
    for i in nums:
        if ans == []:
            ans.append(i)
        else:
            ans.append(i + ans[-1])
    return ans

print(test([2,3,0,2]))

# runtime 28 ms, 14.4 MB memory