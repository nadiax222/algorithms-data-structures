# Doubly Linked List in Python

A Python implementation of a doubly linked list.

The project demonstrates how linked lists work internally by using nodes connected in both directions.

Each node stores:

- a value,
- a reference to the next node,
- a reference to the previous node.

## Project goal

The purpose of this project is to practise:

- object-oriented programming,
- classes and objects,
- references between objects,
- dynamic data structures,
- insertion and deletion operations,
- searching in a linked list,
- traversing a list in both directions.

## What is a doubly linked list?

A doubly linked list is a sequence of nodes.

Each node contains:

```text
key
next
prev
```

Where:

- `key` stores the value,
- `next` points to the next node,
- `prev` points to the previous node.

Example:

```text
None ← [3] ⇄ [2] ⇄ [4] ⇄ [1] → None
         ↑                       ↑
        head                    tail
```

The list stores two references:

```text
head
tail
```

- `head` points to the first node,
- `tail` points to the last node.

## Implemented operations

The project implements the following methods:

- `is_empty()` — checks whether the list is empty,
- `insert(key)` — inserts a new node at the beginning,
- `search(key)` — searches for a node,
- `insert_after(new_key, searched_key)` — inserts a node after another node,
- `insert_before(new_key, searched_key)` — inserts a node before another node,
- `delete(key)` — deletes the first node containing the selected value,
- `write()` — displays the list from head to tail,
- `write_reverse()` — displays the list from tail to head,
- `clear()` — removes all nodes from the list.

## Node class

The `Node` class represents one list element.

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None
```

Each node stores its value and references to neighbouring nodes.

## DoublyLinkedList class

The list begins with no nodes:

```python
self.head = None
self.tail = None
```

When the first node is added, it becomes both the head and the tail.

## Inserting at the beginning

The method:

```python
insert(key)
```

adds a new node at the beginning of the list.

Example:

```python
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
```

Result:

```text
3 2 1
```

Each new value becomes the new head.

## Searching

The method:

```python
search(key)
```

starts at the head and moves through the list using `next`.

If the node is found, the method returns it.

If the value is not present, it returns:

```python
None
```

Example:

```python
result = linked_list.search(2)
```

## Inserting after a selected node

The method:

```python
insert_after(new_key, searched_key)
```

inserts a new value after an existing value.

Example:

```text
Before:
3 2 1
```

Operation:

```python
linked_list.insert_after(4, 2)
```

Result:

```text
3 2 4 1
```

## Inserting before a selected node

The method:

```python
insert_before(new_key, searched_key)
```

inserts a new value before an existing value.

Example:

```text
Before:
3 4 1
```

Operation:

```python
linked_list.insert_before(5, 3)
```

Result:

```text
5 3 4 1
```

## Deleting a node

The method:

```python
delete(key)
```

removes the first node containing the selected value.

Example:

```text
Before:
3 2 4 1
```

Operation:

```python
linked_list.delete(2)
```

Result:

```text
3 4 1
```

The method reconnects the previous and next nodes.

If the deleted node is the head or tail, the corresponding reference is updated.

## Forward traversal

The method:

```python
write()
```

starts at `head` and follows `next`.

Example:

```text
5 3 4 1
```

## Reverse traversal

The method:

```python
write_reverse()
```

starts at `tail` and follows `prev`.

Example:

```text
1 4 3 5
```

This demonstrates the main advantage of a doubly linked list: it can be traversed in both directions.

## Clearing the list

The method:

```python
clear()
```

disconnects all nodes and sets:

```python
self.head = None
self.tail = None
```

After clearing, the list is empty.

## Example output

```text
Initial list:

After inserting 1 and 2:
2 1

After inserting 3:
3 2 1

Search for 2: 2
Search for 4: -1

After inserting 4 after 2:
3 2 4 1

After deleting 2:
3 4 1

Element 5 was not found.
After attempting to delete 5:
3 4 1

After inserting 5 before 3:
5 3 4 1

List in reverse order:
1 4 3 5

After clearing the list:
```

## Time complexity

| Operation | Complexity |
|---|---:|
| Check if empty | `O(1)` |
| Insert at beginning | `O(1)` |
| Search | `O(n)` |
| Insert after a value | `O(n)` |
| Insert before a value | `O(n)` |
| Delete by value | `O(n)` |
| Display forward | `O(n)` |
| Display backward | `O(n)` |
| Clear | `O(n)` |

Insertion or deletion itself is constant-time once the correct node is known.

However, searching for the node requires up to `O(n)` time.

## Space complexity

The list uses:

```text
O(n)
```

memory, where `n` is the number of nodes.

Each node stores:

- one value,
- one `next` reference,
- one `prev` reference.