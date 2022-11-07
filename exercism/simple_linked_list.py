class Node:
    def __init__(self, value, n=None):
        self._next = n
        self._value = value

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, n):
        self._next = n


class LinkedListIterator:
    def __init__(self, node):
        self._node = node

    def __next__(self):
        if self._node:
            val = self._node.value()
            self._node = self._node.next()
            return val
        raise StopIteration


class LinkedList:

    def __init__(self, values=[]):
        self._length = 0
        self._head = None
        for v in values:
            self.push(v)

    def __len__(self):
        return self._length

    def __iter__(self):
        return LinkedListIterator(self._head)

    def head(self):
        if not self._head:
            raise EmptyListException('The list is empty.')
        return self._head

    def push(self, value):
        self._length += 1
        self._head = Node(value, self._head)

    def pop(self):
        if not self._head:
            raise EmptyListException('The list is empty.')
        val = self._head.value()
        self._head = self._head.next()
        self._length -= 1
        return val

    def reversed(self):
        def rev_helper(l, node):
            if not node:
                return l
            l.push(node.value())
            return rev_helper(l, node.next())
        if not self._head:
            return self
        return rev_helper(LinkedList([self._head.value()]), self._head.next())


class EmptyListException(Exception):
    pass
