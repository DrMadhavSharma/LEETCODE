'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        def merge(l1,l2):
            dummy=Node(0)
            tail=dummy
            while l1 and l2:
                if l1.data<=l2.data:
                    tail.next=l1
                    l1=l1.next
                else:
                    tail.next=l2
                    l2=l2.next
                tail=tail.next
            if l1:
                tail.next=l1
            if l2:
                tail.next=l2
            return dummy.next
        while len(arr) > 1:
            temp = []
            for i in range(0, len(arr)-1, 2):
                temp.append(merge(arr[i], arr[i+1]))
            if len(arr) % 2 == 1:
                temp.append(arr[-1])  # odd one left
            arr = temp
        return arr[0]
                
                

               
            
                    