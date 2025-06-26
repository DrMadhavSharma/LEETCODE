class Solution:
    def isSubsetSum (self, arr, sum):
        n=len(arr)
        t=[[False for _ in range(sum+1)] for _ in range(n+1)]
        for i in range(0,n+1):
            for j in range(0,sum+1):
                if i==0:
                    t[i][j]=False
                if j==0:
                    t[i][j]=True
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    t[i][j]= t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][sum]
    def equalPartition(self, arr):
      n=len(arr)
      sum=0
      for i in range(n):
          sum=sum+arr[i]
      if(sum%2!=0):
          return False
      else:
          return self.isSubsetSum(arr,sum//2)