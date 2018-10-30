def bracket_match(text):
    count = 0
    lst = []
    for t in text:
        if t == '(':
            lst.append(t)
        else:
            if not lst:
                count += 1
            else:
                tem = lst.pop()
    return count+len(lst)


assert bracket_match(')') == 1
assert bracket_match('(') == 1
assert bracket_match('()') == 0
assert bracket_match(')(') == 2
assert bracket_match('(()') == 1
assert bracket_match('())(') == 2
