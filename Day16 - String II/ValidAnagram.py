class Solution(object):
    def isAnagram(self, s, t):
        hash_table_s = {}
        hash_table_t = {}

        for ch in s:
            if ch not in hash_table_s:
                hash_table_s[ch] = 1
            else:
                hash_table_s[ch] += 1

       # print(hash_table_s)

        for ch in t:
            if ch not in hash_table_t:
                hash_table_t[ch] = 1
            else:
                hash_table_t[ch] += 1

       # print(hash_table_t)
        print(hash_table_t == hash_table_s)

solution = Solution()
s = "anagram"
t = "nagaram"
solution.isAnagram(s,t)
