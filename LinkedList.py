class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def LinkedListInsert(head, index, value):
    if index == 0:
        new_head = LinkedListNode(value)
        new_head.next = head
        return new_head

    current = head
    previous = None
    count = 0

    while count < index and current is not None:
        previous = current
        current = current.next
        count += 1

    if count < index:
        raise ValueError("Produce an invalid index error")

    new_node = LinkedListNode(value)
    new_node.next = previous.next
    previous.next = new_node

    return head

def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = None
head = LinkedListInsert(head, 0, 10)
head = LinkedListInsert(head, 1, 20)
head = LinkedListInsert(head, 2, 30)

print_list(head)