class Solution:
    def isValid(self, s: str) -> bool:
        class Stack:
            def __init__(self):
                self.items = []
            def push(self, e):
                self.items.append(e)
            def pop(self):
                return self.items.pop()
            def is_empty(self):
                return len(self.items) == 0
            def peek(self):
                if not self.is_empty():
                    return self.items[-1]
            def size(self):
                return len(self.items)

        hashdic = {'(': ')', '{': '}', '[': ']'}
        obj = Stack()

        for i in s:
            if i in hashdic:
                obj.push(i)
            elif i in hashdic.values():
                if obj.is_empty():
                    return False
                top = obj.peek()
                if hashdic[top] == i:
                    obj.pop()
                else:
                    return False

        return obj.is_empty()
