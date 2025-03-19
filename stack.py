class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop()) 
print(stack.pop())  