def test(candies: list, extraCandies):
    ans = []
    for i in candies:
        if i + extraCandies >= max(candies):
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(test([5,1,3], 3))

# not sure why this isnt working, it gives the proper output when testing with REPL
# lol it was because i used 'False' instead of False
# runtime 40 ms, 14.3 MB memory