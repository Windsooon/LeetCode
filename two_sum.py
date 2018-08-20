class Solution:
    # @return a tuple, (index1, index2)
    # [2, 7, 11, 15] target=9
    def twoSum(self, num, target):
        hash_dist = {}
        for index, value in enumerate(num):
            last = target - value
            if last in hash_dist:
                return hash_dist[last], index
            hash_dist[value] = index
if __name__ == "__main__":
    solution = Solution()
    num = [2,7, 11, 15]
    target = 18
    print(solution.twoSum(num, target))
