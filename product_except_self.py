from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            nums.remove()


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums = [1,2,4,6]))
    # Output: [48,24,12,8]
    print(solution.productExceptSelf(nums = [-1,0,1,2,3]))
    # Output: [0,-6,0,0,0]