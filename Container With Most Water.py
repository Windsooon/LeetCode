'''
The graph look like this, We set two points at the first and the last element, then keep compare two value, than move the pointer which own the least value.  
    y 
    |
    |     a2
    |     |  a3          an
    |  a1 |  |     a5    | 
    |  |  |  |  a4 |     |
    |  |  |  |  |  | ..  |
    --------------------------->
    0   1  2  3  4  5 ..  n     x

    (graph from fullmetal2000)


How can we geneentate we will not miss the max value, for instance, the indexes of the greatest value is i, j.

    ans = min(a<i>, a<j>)x(j-i)

When we move the pointer from the first and the last element. We will meet one of i or j. Let's assume the pointer meet i first (it doesn't metter which you meet first.). Let's assume we miss the correct index, when the left pointer in i, the right pointer in j+k. Then follow our rule, i < j+k, then we move the left pointer.In this situation:

    ans > min(a<i>, a<j+k>) * (j-i+k)
 and because of a(j+k) > a(i)
    ans > a<i> * (j-i+k)  (3)

if a<i> <= a<j>:
   ans = a<i> * (j-i)

'''
class Solution:
    # two pointer
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height)-1
        max_count = 0
        while left < right:
            max_count = max(max_count, min(height[left], height[right]) * (right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_count
