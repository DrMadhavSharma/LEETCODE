class Solution:
    def romanToInt(self, s: str) -> int:
        symbol=['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value=[1,5,10,50,100,500,1000]
        dct=dict(zip(symbol,value))
        sol=0
        for i in range(len(s) - 1):
            elem = s[i]
            nxt = s[i + 1]
            if symbol.index(elem) < symbol.index(nxt):
                sol += dct[nxt] - dct[elem]
                sol -= dct[nxt]  # to cancel the double addition
            else:
                sol += dct[elem]
        sol += dct[s[-1]]  # add the last character
        return sol