class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = ""
        n = len(strs)
        dic = {}
        for i in range(n):
            dic[i] = list(strs[i])
        for j in range(len(dic[0])):
            ch = dic[0][j]
            match = True
            for k in range(1, n):
                if j >= len(dic[k]) or dic[k][j] != ch:
                    match = False
                    break
            if match:
                sol += ch
            else:
                break
        return sol