import collections

class Solution:
    def findRestaurant(self, list1, list2):
        dic = collections.defaultdict(int)
        for i in range(len(list1)):
            dic[list1[i]] += i
        for i in range(len(list2)):
            dic[list2[i]] += i
        min_index = float('inf')
        ans = ''
        for k, v in dic.items():
            if v < min_index:
                ans = k
                min_index = v
        return ans
                
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

s = Solution()
print(s.findRestaurant(list1, list2))
