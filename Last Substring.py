def compute(s):
    # Write your code here
    index = 0
    max_val = ord('a') - 1
    for i in range(len(s)):
        if ord(s[i]) > max_val:
            max_val = ord(s[i])
            index = i
    return s[index:]


assert compute('ab') == 'b'
assert compute('ba') == 'ba'
assert compute('banana') == 'nana'
assert compute('aaa') == 'aaa'
assert compute('') == ''
