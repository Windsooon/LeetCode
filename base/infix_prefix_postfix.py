# infix                    prefix          postfix
# a + b * c               + a * b c       a b c * +
# a ∗ (b + c)             * a + b c       a b c + *
# a / b + c / d           + / a b / c d   a b / c d / +
# (a + b) ∗ (c + d)       * + a b + c d   a b + c d + *
# ((a + b) ∗ c) - d       - * + a b c d   a b + c * d -

def infix_to_postfix(string):
    string = string.split(' ')
    res, stack = [], []
    string = ['('] + string + [')']
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            while 1:
                top = stack.pop()
                if top == '(':
                    break
                else:
                    res.append(top)
        elif string[i] in '+-':
            while stack and stack[-1] in '*/+-':
                top = stack.pop()
                res.append(top)
            stack.append(string[i])
        elif string[i] in '*/':
            while stack and stack[-1] in '*/':
                top = stack.pop()
                res.append(top)
            stack.append(string[i])
        else:
            res.append(string[i])
    return ' '.join(res)

# print(infix_to_postfix('a + b * c'))
# print(infix_to_postfix('a * ( b + c )'))
# print(infix_to_postfix('a / b + c / d'))
# print(infix_to_postfix('( a + b ) * ( c + d )'))
# print(infix_to_postfix('( ( a + b ) * c ) - d'))

def infix_to_prefix(string):
    string = string.split(' ')
    res, stack = [], []
    string = ['('] + string + [')']
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            while 1:
                top = stack.pop()
                if top == '(':
                    break
                else:
                    second = res.pop()
                    first = res.pop()
                    res.append(top + first + second)
        elif string[i] in '+-':
            while stack and stack[-1] in '*/+-':
                top = stack.pop()
                second = res.pop()
                first = res.pop()
                res.append(top + first + second)
            stack.append(string[i])
        elif string[i] in '*/':
            while stack and stack[-1] in '*/':
                top = stack.pop()
                second = res.pop()
                first = res.pop()
                res.append(top + first + second)
            stack.append(string[i])
        else:
            res.append(string[i])
    return ' '.join(res)

print(infix_to_prefix('a + b * c'))
print(infix_to_prefix('a * ( b + c )'))
print(infix_to_prefix('a / b + c / d'))
print(infix_to_prefix('( a + b ) * ( c + d )'))
print(infix_to_prefix('( ( a + b ) * c ) - d'))
