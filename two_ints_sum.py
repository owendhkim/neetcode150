from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm:
                return sorted([i,hm[target - nums[i]]])
            else:
                hm[nums[i]] = i;
                       
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums = [3,4,5,6], target = 7))
    print(solution.twoSum(nums = [4,5,6], target = 10))
    print(solution.twoSum(nums = [5,5], target = 10))