# Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):  #j 自动驱动j
            if s[j] in mp: 
                i = max(mp[s[j]], i) #如果有重复的字母，i就直接skip到除了这个字母的下一个index

            ans = max(ans, j - i + 1)  #积累最长的substring， j-i + 1 ， +1是因为起点为0
            mp[s[j]] = j + 1  #给字母map 标记要跳的index

        return ans
    
    #method 2
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        word = ""
        for c in s:
            if c not in word:
                word += c
                print("if word: " + word)
                if len(word) > res:
                    res = len(word)
                    print(res)
            else:
                print(word)  #abcf
                word = word[word.find(c) + 1:] + c #fc
                print(word.find(c)) #1
                
                
        return res
one =Solution();
print(one.lengthOfLongestSubstring("abcfcde"))
