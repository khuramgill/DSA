class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

# Example Usage:
if __name__ == '__main__':
    
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(55)
    
    print("Stack:", my_stack.items)
    print("Peek:", my_stack.peek())
    popped_item = my_stack.pop()
    print("IsEmpty: ",my_stack.is_empty())
    print("Stack after popping:", my_stack.items)
    print("Popped Item:", popped_item)
    print("Peek:", my_stack.peek())
