class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        pretty_list = ""
        for element in self.stack:
            pretty_list += f"{element} -> "
        return pretty_list

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop[-1]


    def is_empty(self):
       return len(self.stack)

    def peek(self):
        return self.stack[-1]



    def size(self):
        return len(self.stack)


if __name__ == "__main__":

    my_stack = Stack()

    my_stack.push(3)
    print(my_stack)
    my_stack.push(2)
    print(my_stack)
    my_stack.push(1)
    print(my_stack)
