class Solution(object):
    def simplifyPath(self, path):
        stack = []
        place = [p for p in path.split('/') if p != '' and p != '.']
        for p in place:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath('/home/'))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/a/../../b/../c//.//"))
print(s.simplifyPath("/a//b////c/d//././/.."))
print(s.simplifyPath("/../"))
