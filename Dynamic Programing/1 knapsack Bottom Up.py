class Solution:
    def __init__(self):
        self.t = None
    def knapsack(self, W, val, wt,n=None):
        if n is None:
            n=len(val)
        if  self.t is None:
            self.t=[[-1]*(W+1) for _ in range(n+1)]
        
        if n==0 or W==0:
            return 0
        if (self.t[n][W]!=-1):
            return self.t[n][W]
        
        if(wt[n-1]<=W):
            self.t[n][W]=max(val[n-1]+self.knapsack(W-wt[n-1],val,wt,n-1),
            self.knapsack(W,val,wt,n-1))
        else:
            self.t[n][W]=self.knapsack(W,val,wt,n-1)
        
        return self.t[n][W]
