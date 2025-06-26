class Solution:
    def knapsack(self, W, val, wt):
        n=len(wt)
        t=[[0 for _ in range(W+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,j+1):
                if (wt(i-1)<=j):
                    t[i-1][j]=max(val[i-1]+t[i-1][j-wt[i-1],t[i-1][j]])
                else:
                    t[i][j]=t[i-1][j]
        return t[n][W]