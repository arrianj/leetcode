# Number of Good Pairs

def test(nums: list):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count

print(test([1,1,1,1]))

# runtime 36 ms, 14.3 MB memory