class Node:
    # Represents one element of a doubly linked list.

    def __init__(self, key):
        self.key = key
        # Value stored in the node.

        self.next = None
        # Reference to the next node.

        self.prev = None
        # Reference to the previous node.


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        # Reference to the first node.

        self.tail = None
        # Reference to the last node.

    def is_empty(self):
        # Checks whether the list is empty.
        return self.head is None

    def insert(self, key):
        # Inserts a new node at the beginning of the list.
        # Corresponds to LIST-INSERT(L, key).

        new_node = Node(key)

        if self.is_empty():
            # If the list is empty, the new node becomes
            # both the first and the last node.
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        # The new node points to the previous first node.

        self.head.prev = new_node
        # The previous first node points back to the new node.

        self.head = new_node
        # The new node becomes the first node.

    def search(self, key):
        # Searches for a node containing the given key.
        # Corresponds to LIST-SEARCH(L, key).
        # Returns the node if found.
        # Returns None if the key is not present.

        current = self.head

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def insert_after(self, new_key, searched_key):
        # Inserts new_key after the node containing searched_key.
        # Corresponds to LIST-INSERT-AFTER(
        # L, new_key, searched_key
        # ).

        searched_node = self.search(searched_key)

        if searched_node is None:
            print(
                f"Element {searched_key} was not found."
            )
            return False

        new_node = Node(new_key)

        new_node.prev = searched_node
        # The new node points back to the searched node.

        new_node.next = searched_node.next
        # The new node points to the node that was previously next.

        if searched_node.next is not None:
            searched_node.next.prev = new_node
            # The next node points back to the new node.
        else:
            self.tail = new_node
            # If the searched node was the last node,
            # the new node becomes the new tail.

        searched_node.next = new_node
        # The searched node points to the new node.

        return True

    def insert_before(self, new_key, searched_key):
        # Inserts new_key before the node containing searched_key.
        # Corresponds to LIST-INSERT-BEFORE(
        # L, new_key, searched_key
        # ).

        searched_node = self.search(searched_key)

        if searched_node is None:
            print(
                f"Element {searched_key} was not found."
            )
            return False

        new_node = Node(new_key)

        new_node.next = searched_node
        # The new node points to the searched node.

        new_node.prev = searched_node.prev
        # The new node points back to the previous node.

        if searched_node.prev is not None:
            searched_node.prev.next = new_node
            # The previous node points to the new node.
        else:
            self.head = new_node
            # If the searched node was the first node,
            # the new node becomes the new head.

        searched_node.prev = new_node
        # The searched node points back to the new node.

        return True

    def delete(self, key):
        # Deletes the first node containing the given key.
        # Corresponds to LIST-DELETE(L, key).

        node_to_delete = self.search(key)

        if node_to_delete is None:
            print(
                f"Element {key} was not found."
            )
            return False

        if node_to_delete.prev is not None:
            node_to_delete.prev.next = node_to_delete.next
            # The previous node skips the deleted node.
        else:
            self.head = node_to_delete.next
            # If the first node is deleted,
            # head moves to the next node.

        if node_to_delete.next is not None:
            node_to_delete.next.prev = node_to_delete.prev
            # The next node skips the deleted node.
        else:
            self.tail = node_to_delete.prev
            # If the last node is deleted,
            # tail moves to the previous node.

        node_to_delete.next = None
        node_to_delete.prev = None
        # Disconnects the deleted node from the list.

        return True

    def write(self):
        # Displays the current list from head to tail.

        current = self.head
        elements = []

        while current is not None:
            elements.append(str(current.key))
            current = current.next

        print(" ".join(elements))

    def write_reverse(self):
        # Displays the list from tail to head.
        # Demonstrates the purpose of prev.

        current = self.tail
        elements = []

        while current is not None:
            elements.append(str(current.key))
            current = current.prev

        print(" ".join(elements))

    def clear(self):
        # Removes all nodes from the list.
        # Corresponds to CLEAR(L).

        current = self.head

        while current is not None:
            next_node = current.next

            current.next = None
            current.prev = None

            current = next_node

        self.head = None
        self.tail = None


def test_list():
    # Runs the operations shown in the assignment example.

    linked_list = DoublyLinkedList()

    print("Initial list:")
    linked_list.write()
    # Empty list.

    linked_list.insert(1)
    linked_list.insert(2)

    print("After inserting 1 and 2:")
    linked_list.write()
    # Expected output: 2 1

    linked_list.insert(3)

    print("After inserting 3:")
    linked_list.write()
    # Expected output: 3 2 1

    result = linked_list.search(2)

    if result is not None:
        print("Search for 2:", result.key)
    else:
        print("Search for 2: -1")

    result = linked_list.search(4)

    if result is not None:
        print("Search for 4:", result.key)
    else:
        print("Search for 4: -1")

    linked_list.insert_after(4, 2)

    print("After inserting 4 after 2:")
    linked_list.write()
    # Expected output: 3 2 4 1

    linked_list.delete(2)

    print("After deleting 2:")
    linked_list.write()
    # Expected output: 3 4 1

    linked_list.delete(5)

    print("After attempting to delete 5:")
    linked_list.write()
    # Expected output: 3 4 1

    linked_list.insert_before(5, 3)

    print("After inserting 5 before 3:")
    linked_list.write()
    # Expected output: 5 3 4 1

    print("List in reverse order:")
    linked_list.write_reverse()
    # Expected output: 1 4 3 5

    linked_list.clear()

    print("After clearing the list:")
    linked_list.write()
    # Empty list.


if __name__ == "__main__":
    test_list()