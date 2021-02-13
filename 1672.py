def test(accounts: list[list[int]]):
    maxwealth = []
    for account in accounts:
        maxwealth.append(sum(account))
    return max(maxwealth)

# this one made me remember its not always "for i in blah blah"
# slow down. think about it.
# runtime 56 ms, 14.1 MB memory