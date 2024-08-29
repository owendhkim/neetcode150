from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        ans = []
        for num in nums:
            if num in hm:
                hm[num] = hm[num] + 1
            else:
                hm[num] = 1
        sorted_by_values = dict(sorted(hm.items(), key=lambda item: item[1]))
        key_list_sorted_by_values = list(sorted_by_values.keys())
        for i in range(k):
            last_element = key_list_sorted_by_values.pop()
            ans.append(last_element)
        return ans
    # time complexity = O(nlogn) because of sorting
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        buckets = [[] for i in range(len(nums) + 1)]
        ans = []
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        for key, value in hm.items():
            buckets[value].append(key)
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i] != []:
                ans.append(buckets[i][0])
                if len(ans) == k:
                    return ans
        # time complexity = O(n)

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent2([1,2,2,3,3,3], k = 2))
    print(solution.topKFrequent2([7,7], k = 1))