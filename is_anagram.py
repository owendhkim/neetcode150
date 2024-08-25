# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         l = list(s)
#         for char in t:
#             if char in l:
#                 l.remove(char)
#                 # .remove() has to search for the element to remove
#                 # linear search, worst case O(n)
#         if len(l) == 0:
#             return True
#         else:
#             return False
#         # time complexcity = O(n * m)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         hm_s = {}
#         hm_t = {}
#         for char in s:
#             hm_s[char] = hm_s.get(char, 0) + 1
#         for char in t:
#             hm_t[char] = hm_t.get(char, 0) + 1
#         for char in s:
#             if hm_s[char] != hm_t.get(char, 0):
#                 return False
#         return True
#     # time complexity = O(n + m)
#     # space complexity = O(number of unique characters in str s & t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram(s="racecar", t="carrace"))
    print(solution.isAnagram(s="jar", t="jam"))