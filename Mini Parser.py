class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return
        if s[0] != '[':
            return NestedInteger(s)
        current = None
        num = 0
        for i in range(len(s)):
            if s[i] == '[':
                if not current:
                    current = NestedInteger()
                else:
                    current.add(self.deserialize(s[i:]))
            elif s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == ',':
                current.add(NestedInteger(num))
                num = 0
            elif s[i] == ']':
                if num:
                    current.add(NestedInteger(num))
                return current
