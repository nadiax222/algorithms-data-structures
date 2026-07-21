class Stack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        # Array with empty positions, for example:
        # [None, None, None, None, None]

        self.top = 0
        # The stack is empty.
        # top also stores the number of elements currently on the stack.

    def is_empty(self):
        return self.top == 0
        # Returns True when the stack is empty.

    def push(self, value):
        # Adds an element to the top of the stack.

        if self.top == self.capacity:
            print("excess")
            return
            # The stack is full, so no more elements can be added.

        self.data[self.top] = value
        # Inserts the value into the first empty position.

        self.top += 1
        # Increases the number of elements on the stack.

    def pop(self):
        # Removes the most recently added element.

        if self.is_empty():
            print("insufficiency")
            return None
            # If the stack is empty, there is nothing to remove.

        self.top -= 1
        # Decreases top so that it points to the last element.

        value = self.data[self.top]
        # Saves the value that will be removed.

        self.data[self.top] = None
        # Clears the position in the array.

        return value
        # Returns the removed element.

    def write(self):
        # Displays the current contents of the stack.

        if self.is_empty():
            print()
        else:
            print(*self.data[:self.top])
            # Selects only occupied positions.
            # The * operator prints elements without brackets and commas.


class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        # Array used to store queue elements.

        self.head = 0
        # Index of the first element to be removed.

        self.tail = 0
        # Index of the position where the next element will be added.

        self.count = 0
        # Number of elements currently in the queue.

    def is_empty(self):
        return self.count == 0
        # If count equals 0, the queue is empty.

    def enqueue(self, value):
        # Adds an element to the end of the queue.

        if self.count == self.capacity:
            print("excess")
            return
            # The queue is full.

        self.data[self.tail] = value
        # Adds the element at the current tail position.

        self.tail = (self.tail + 1) % self.capacity
        # Moves tail to the next position.
        # % means remainder of division.
        # It allows the index to return to 0 after reaching the end.

        self.count += 1
        # Increases the number of elements in the queue.

    def dequeue(self):
        # Removes the first element from the queue.

        if self.is_empty():
            print("insufficiency")
            return None
            # If the queue is empty, there is nothing to remove.

        value = self.data[self.head]
        # Saves the value at the beginning of the queue.

        self.data[self.head] = None
        # Clears the position from which the element was removed.

        self.head = (self.head + 1) % self.capacity
        # Moves head to the next position.
        # The modulo operation makes the queue circular.

        self.count -= 1
        # Decreases the number of elements in the queue.

        return value
        # Returns the removed value.

    def write(self):
        # Displays queue elements in their logical order.

        if self.is_empty():
            print()
            return

        elements = []

        for i in range(self.count):
            # Runs as many times as there are elements in the queue.

            index = (self.head + i) % self.capacity
            # Calculates the correct position in the circular queue.

            elements.append(self.data[index])
            # Adds the element in the correct logical order.

        print(*elements)
        # Prints elements without brackets and commas.


def test_stack():
    print("STACK")

    stack = Stack(5)

    stack.push(1)
    stack.push(2)
    stack.write()
    # Output: 1 2

    stack.push(3)
    stack.write()
    # Output: 1 2 3

    print(stack.is_empty())
    # Output: False

    stack.push(4)
    stack.push(5)
    stack.push(6)
    # Output: excess, because the stack capacity is 5.

    print(stack.pop())
    # Output: 5

    print(stack.pop())
    # Output: 4

    print(stack.pop())
    # Output: 3

    print(stack.pop())
    # Output: 2

    stack.write()
    # Output: 1

    print(stack.pop())
    # Output: 1

    stack.pop()
    # Output: insufficiency
    # It is not placed inside print(), because otherwise None
    # would also be displayed.

    stack.write()
    # Empty line because the stack is empty.

    print(stack.is_empty())
    # Output: True


def test_queue():
    print("\nQUEUE")

    queue = Queue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.write()
    # Output: 1 2

    queue.enqueue(3)
    queue.write()
    # Output: 1 2 3

    print(queue.is_empty())
    # Output: False

    print(queue.dequeue())
    # Output: 1

    print(queue.dequeue())
    # Output: 2

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    # Output: excess, because the queue capacity is 5.

    queue.write()
    # Output: 3 4 5 6 7

    print(queue.dequeue())
    # Output: 3

    print(queue.dequeue())
    # Output: 4

    print(queue.dequeue())
    # Output: 5

    print(queue.dequeue())
    # Output: 6

    print(queue.dequeue())
    # Output: 7

    queue.dequeue()
    # Output: insufficiency
    # It is not placed inside print(), because otherwise None
    # would also be displayed.

    queue.write()
    # Empty line because the queue is empty.

    print(queue.is_empty())
    # Output: True


if __name__ == "__main__":
    test_stack()
    test_queue()