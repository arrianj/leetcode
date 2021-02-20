# Height Checker

def test(heights: list):
    moved = 0

    sortedlist = sorted(heights)

    for idx, i in enumerate(heights):
        if i != sortedlist[idx]:
            moved += 1
    return moved

print(test([5,1,2,3,4]))

# runtime 32 ms, 14.2 MB memory