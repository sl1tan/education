class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def append(self, value):
        end = Node(value)
        head = self
        while(head.next):
            head = head.next
        head.next = end
    def print_node(self):
        head = self
        print(head.data, end = " ")
        while(head.next):
            head = head.next
            print(head.data, end = " ")
        print()


ll = Node(0)
ll.append(1)
ll.append(2)
ll.print_node()