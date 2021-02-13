def reformatNumber(number: str):
    ans = ''
    parts = []
    numerals = '1234567890'
    for i in number:
        if i in numerals:
            ans += i
    while len(ans) > 4:
        parts.append(ans[:3])
        ans = ans[3:]
    if len(ans) <= 3:
        parts.append(ans)
    else:
        parts.append(ans[:2])
        parts.append(ans[2:])

    return '-'.join(parts)


# figuring out the final digit grouping was tricky
# think about what NEEDS to happen, work backwards from there
# runtime 24 ms, 14.3 MB memory