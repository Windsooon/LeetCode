def permutations(lst):
    return_lst = []
    helper([], lst, return_lst)
    return return_lst


def helper(current, choices, return_lst):
    # [], [1, 2, 3, 4], []
    if not choices:
        return_lst.append(choices)
        return
    for c in choices:
        if c not in current:
            current.append(c)
            choices.remove(c)
            helper(current, choices, return_lst)
            current.remove(c)
            choices.append(c)


# def good_permutation(list, start, end):
#     '''This prints all the permutations of a given list
#        it takes the list,the starting and ending indices as input'''
#     if (start == end):
#         pass
#     else:
#         # 0, 3
#         for i in range(start, end + 1):
#             list[start], list[i] = list[i], list[start]  # The swapping
#             good_permutation(list, start + 1, end)
#             list[start], list[i] = list[i], list[start]  # Backtracking
# 
# good_permutation([1, 2, 3], 0, 2)

print(permutations([1, 2, 3, ]))
