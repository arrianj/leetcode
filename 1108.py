def test(address: str):
    new = ''
    for i in address:
        if i in '1234567890':
            new += i
        elif i in '.':
            new += '[.]'
    return new

print(test('123.123'))

# 20 ms runtime, 14.4 MB memory