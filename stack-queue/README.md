# Stack and Circular Queue in Python

A simple Python project implementing two fundamental data structures:

- a stack,
- a circular queue.

Both structures use fixed-size arrays and support basic operations such as adding, removing, checking whether the structure is empty, displaying its contents, and handling overflow and underflow.

## Project goal

The purpose of this project is to understand how stacks and queues work internally without using Python's built-in stack or queue classes.

The project demonstrates:

- array-based data structures,
- LIFO and FIFO behaviour,
- fixed capacity,
- overflow handling,
- underflow handling,
- circular indexing,
- classes and methods in Python.

## Stack

A stack works according to the LIFO rule:

```text
Last In, First Out
```

This means that the last element added is the first one removed.

Example:

```text
Push: 1
Push: 2
Push: 3

Stack:
1 2 3

Pop:
3
```

### Implemented stack operations

- `is_empty()` — checks whether the stack is empty,
- `push(value)` — adds an element to the top,
- `pop()` — removes the most recently added element,
- `write()` — displays all stack elements.

### Stack structure

The stack uses:

```python
self.data
```

to store values and:

```python
self.top
```

to store the number of elements and indicate the next free position.

Example:

```text
data = [1, 2, 3, None, None]
top = 3
```

## Queue

A queue works according to the FIFO rule:

```text
First In, First Out
```

This means that the first element added is the first one removed.

Example:

```text
Enqueue: 1
Enqueue: 2
Enqueue: 3

Queue:
1 2 3

Dequeue:
1
```

### Implemented queue operations

- `is_empty()` — checks whether the queue is empty,
- `enqueue(value)` — adds an element to the end,
- `dequeue()` — removes the first element,
- `write()` — displays queue elements in logical order.

## Circular queue

The queue is implemented as a circular queue.

It uses:

```python
self.head
```

to indicate the first element,

```python
self.tail
```

to indicate the next free position,

and:

```python
self.count
```

to store the number of elements.

The index is moved using:

```python
(self.tail + 1) % self.capacity
```

or:

```python
(self.head + 1) % self.capacity
```

The modulo operator `%` makes the index return to `0` after reaching the end of the array.

Example for capacity `5`:

```text
(4 + 1) % 5 = 0
```

This allows the queue to reuse positions that were freed by earlier `dequeue()` operations.

## Overflow and underflow

### Overflow

Overflow occurs when an element is added to a full structure.

The program displays:

```text
excess
```

Example:

```text
Stack capacity: 5
Attempt to push a sixth element
Output: excess
```

### Underflow

Underflow occurs when an element is removed from an empty structure.

The program displays:

```text
insufficiency
```

Example:

```text
Empty queue
Attempt to dequeue
Output: insufficiency
```

## Program tests

The project contains two test functions:

```python
test_stack()
test_queue()
```

### Stack test

The stack test:

1. adds values `1`, `2`, and `3`,
2. displays the stack,
3. checks whether it is empty,
4. fills it to capacity,
5. attempts to add one more element,
6. removes all elements,
7. attempts to remove from an empty stack,
8. checks whether the stack is empty.

### Queue test

The queue test:

1. adds values `1`, `2`, and `3`,
2. displays the queue,
3. removes `1` and `2`,
4. adds `4`, `5`, `6`, and `7`,
5. attempts to add `8`,
6. displays the queue,
7. removes all elements in FIFO order,
8. attempts to remove from an empty queue,
9. checks whether the queue is empty.

## Example output

```text
STACK
1 2
1 2 3
False
excess
5
4
3
2
1
1
insufficiency

True

QUEUE
1 2
1 2 3
False
1
2
excess
3 4 5 6 7
3
4
5
6
7
insufficiency

True
```