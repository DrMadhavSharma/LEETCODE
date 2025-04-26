class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_={}
        
        for i,num in enumerate(nums):
            calculate=target-num
            if calculate in dict_:
                return(dict_[calculate],i)
            else:
                dict_[num]=i
