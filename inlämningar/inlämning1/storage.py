class Node:
    def __init__(self, data):
        """ Store the data, and set next to None"""
        self.data = data
        self.next = None

    def __str__(self):
        """ Return a string representation of the data """
        return str(self.data)


class Storage:
    def __init__(self):
        """ Creates an empty Storage class. Sets head to None. """
        self.head = None
        self.size = 0

    def __str__(self):
        node = self.head
        my_str = ""

        while node is not None:
            my_str += f"{node.data} -> "
            node = node.next

        my_str += "None"
        return my_str

    def __len__(self):
        return self.size

    def push(self, data):
        """ Create a Node to hold the data, then put it at the head of the list. """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.head is None:
            self.head = new_node

        self.size += 1

    def pop(self):
        """ Remove the head Node and return its data. """
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next

        return data

    def peek(self):
        """ Return the data from the head Node, without removing it. """
        if self.head is None:
            return None

        return self.head.data

    def isempty(self):
        """ Return True if the list is empty, otherwise False """
        return len(self) == 0


if __name__ == '__main__':
    stor = Storage()
    print(stor)

    stor.push(1)
    print(stor)
    stor.push(5)
    print(stor)
    stor.push(10)
    print(stor)

    stor.pop()
    print(stor)

    print("The head is:", stor.peek())
    stor.pop()
    stor.pop()
    print("The head is:", stor.peek())

    print("The list is empty:", stor.isempty())