class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        buildings.append([float('inf'), float('inf'), 1])
        stack = [buildings[0]]
        # For in every element
        for index in range(1, len(buildings)):
            # If the left is bigger than the prev's right
            if buildings[index][0] > stack[-1][1]:
                # Insert an empty one
                max_right = max(stack[-1][1], buildings[index-1][1])
                stack.append([max_right, max_right, 0])
                stack.append(buildings[index])
            # overlab of equal
            else:
                if buildings[index][2] > stack[-1][2]:
                    if buildings[index][0] == stack[-1][0]:
                        stack.pop()
                    stack.append(buildings[index])
                elif buildings[index][2] == stack[-1][2]:
                    stack[-1][1] = max(stack[-1][1], buildings[index][1])
                else:
                    if buildings[index][1] > stack[-1][1]:
                        stack.append(
                            [stack[-1][1], stack[-1][1], buildings[index][2]])
        ans = []
        for s in stack:
            ans.append([s[0], s[2]])
        return ans[:-1]


s = Solution()
input = [[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]
print(s.getSkyline(input))
