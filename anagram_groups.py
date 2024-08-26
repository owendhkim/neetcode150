from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        grouped_hm = {}
        if len(strs) == 0:
            return [[]]
        else:
            for s in strs:
                sorted_str = ''.join(sorted(s))
                if sorted_str not in grouped_hm:
                    grouped_hm[sorted_str] = []
                grouped_hm[sorted_str].append(s)
        return grouped_hm.values()
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        grouped_hm = defaultdict(list)
        if len(strs) == 0:
            return [[]]
        else:
            for s in strs:
                sorted_str = ''.join(sorted(s))
                grouped_hm[sorted_str].append(s)
        return grouped_hm.values()


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams1(strs = ["act","pots","tops","cat","stop","hat"]))
    # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    print(solution.groupAnagrams1(strs = ["x"]))
    # Output: [["x"]]
    print(solution.groupAnagrams1(strs = [""]))
    # Output: [[""]]
