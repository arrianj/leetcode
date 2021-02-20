# Split a String in Balanced Strings

def test(string: str):
    count = 0
    splits = 0
    for i in string:
        if i == 'L':
            count += 1
        if i == 'R':
            count -= 1
        if count == 0:
            splits += 1
    return splits

# runtime 32 ms, 14.2 MB memory