from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity - 1
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length <= self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current and self.current.next:
                self.current = self.current.next

                self.current.value = item
            else:
                self.storage.head.value = item
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        list_buffer_contents.append(node.value)

        while node.next:
            node = node.next
            list_buffer_contents.append(node.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass



# buffer = RingBuffer(5)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# print(buffer.get()) # ['a', 'b', 'c', 'd']

# buffer.append('e')
# print(buffer.get()) # ['a', 'b', 'c', 'd', 'e']

# buffer.append('f')
# print(buffer.get()) # ['f', 'b', 'c', 'd', 'e']

# buffer.append('g')
# buffer.append('h')
# buffer.append('i')
# print(buffer.get()) # ['f', 'g', 'h', 'i', 'e']