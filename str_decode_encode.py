from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for s in strs:
            sentence = sentence + str(len(s)) + "#" + s
        return sentence

    def decode(self, s: str) -> List[str]:
        count = ""
        ans = []
        word = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                for j in range(int(count)):
                    word += s[1 + j + i]
                ans.append(word)
                i += int(count)  
                count = ""
                word = "" 
            else:
                count += s[i]      
            i += 1        
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.encode(strs = ["we","say",":","yes","!@#$%^&*()"]))
    print(solution.decode(solution.encode(["we","say",":","yes","!@#$%^&*()"])))
