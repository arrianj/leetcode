# Robot Return to Origin

def test(moves: str):
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    for i in moves:
        if i == 'L':
            end_x -= 1
        if i == 'R':
            end_x += 1
        if i == 'U':
            end_y += 1
        if i == 'D':
            end_y -= 1

    if end_x == start_x and end_y == start_y:
        return True
    else:
        return False

print(test('UDLRUDLR'))

# alternatively, compare number of ups to downs & lefts to rights. if both comparisons are equal, ans = true
# runtime 72 ms, 14.4 MB memory