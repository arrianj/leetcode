def test(nums, n: int):
    ans = []
    i = 0
    j = n
    while i < j:
        ans.append(nums[i])
        ans.append(nums[n])
        i += 1
        n += 1

    return ans

print(test(nums = [1,1,2,2], n = 2))

# runtime 60 ms, 14.4 MB memory