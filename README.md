# DoublyLinkedList – Full Python Implementation with Academic Design

Author: **Giuseppe Muschetta**  
Email: [g.muschetta@studenti.unipi.it](mailto:g.muschetta@studenti.unipi.it)  
University: University of Pisa – MSc in Computer Science  
Specialization: Data Science and Business Informatics  
Date: July 2025  
License: MIT

---

## Overview

This project is a complete, modular, and educational implementation of the **Doubly Linked List** data structure in Python.  
It was developed with academic rigor, clear structure, and professional documentation standards, making it suitable for:

- Data structure education
- Technical interviews
- Python OOP design practice
- Use in stack, queue, or custom memory models

Every feature is demonstrated, tested, and validated using an extensive and structured test suite (`main.py`), acting both as validation and as showcase of the full potential of the class.

---

## Key Features

The `DoublyLinkedList` class supports:

- **Complete Core API**: Full support for all standard list operations: `insert_at_end`, `insert_at_beginning`, `delete_value`, `delete_at_position`, and more.
- **Pythonic by Design**: Integrates seamlessly with Python's idiomatic constructs.
    -   **Iteration**: `for item in my_list:`
    -   **Indexing**: `item = my_list[i]`
    -   **Membership**: `if item in my_list:`
    -   **Sized**: `len(my_list)`
- **Bidirectional traversal** and manipulation
- **Efficient insertion/deletion** at:
  - The beginning
  - The end
  - Arbitrary positions
  - Before/after target nodes
- **Deep cloning** of entire list structure
- **In-place reversal** of node links
- **Duplicate removal** preserving order
- **Sorting** in ascending/descending order using Python-native sorting
- **Search and containment check**
- **Conversion to and from** standard Python lists
- **Versatile & Multi-Purpose**: Can be used directly as other fundamental data structures.
    -   **Stack (LIFO)**: Full stack interface with `push()`, `pop()`, and `peek()`.
    -   **Queue (FIFO)**: Full queue interface with `enqueue()`, `dequeue()`, and `peek_front()`.
- **Robust Error Handling**: Clear and precise exceptions (`IndexError`, `ValueError`, `TypeError`) for predictable behavior and easier debugging.

---

## Pythonic Interface

Fully integrated with Python native constructs:

- `__iter__`, `__reversed__`: iterable and reversible
- `__getitem__`, `__setitem__`: indexable with support for negative indices
- `__contains__`: supports `in` operator
- `__len__`: supports `len()`
- `__str__`, `__repr__`: human-readable and debug-friendly representations
- `__eq__`: equality check between two lists (element-wise)

---

## Stack & Queue Support

The list can be used as a:

- **Stack** (LIFO):
  - `push(value)`
  - `pop()`
  - `peek()`
- **Queue** (FIFO):
  - `enqueue(value)`
  - `dequeue()`
  - `peek_front()`
  - `peek_rear()`

Each behavior is explicitly implemented and demonstrated.

---

## File Structure

```
.
├── node.py                 # Core Node class with info, next, prev
├── doubly_linked_list.py   # Full implementation of DoublyLinkedList
└── main.py                 # Test suite with 23 structured test sections
```

---

## Testing & Validation

The `main.py` script includes over **20 structured sections** of testing covering all:

- Core operations (insertion, deletion)
- Indexing and slicing behavior
- Stack and queue operations
- Reversal and cloning
- Edge cases and exceptions
- Comparisons and deep equality
- Sorting and duplicate handling
- Pythonic features and iterators

Every operation is validated using both `assert` and visual inspection via `print()`, making it suitable for debugging, learning, and showcasing.

---

### Quick Example

```python
from main import DoublyLinkedList

# Create a list from a Python list
dll = DoublyLinkedList.from_python_list([10, 20, 30, 40, 50])

# --- Pythonic Usage ---

# Get size
print(f"Size: {len(dll)}")  # Output: Size: 5

# Get item by index
print(f"Item at index 2: {dll[2]}")  # Output: Item at index 2: 30

# Get a slice
sub_list = dll[1:4]
print(f"Slice from 1 to 4: {sub_list}")  # Output: Slice from 1 to 4: [20, 30, 40]

# Check for membership
print(f"Does it contain 30? {30 in dll}")  # Output: Does it contain 30? True

# --- Use as a Stack ---
dll.push(60)
print(f"Popped from stack: {dll.pop()}")  # Output: Popped from stack: 60

# --- Use as a Queue ---
dll.enqueue(0)
print(f"Dequeued from queue: {dll.dequeue()}")  # Output: Dequeued from queue: 10

---

## Requirements

- Python 3.10+
- No external dependencies

Works on all platforms (Windows, macOS, Linux).

---

## How to Run

```bash
python main.py
```

Ensure that all files are in the same directory:
- `node.py`
- `doubly_linked_list.py`
- `main.py`

---

## Educational Goals

This project was designed for students and professionals aiming to:

- Deepen their understanding of data structures
- Practice clean and modular Python design
- Build reusable, extendable components for personal or academic use

It also serves as an excellent **portfolio project** to demonstrate:
- OOP skills
- Python best practices
- Structured testing
- Functional decomposition

---

## Highlights of Design

- Modularization of `Node` into a separate file
- Safe guards on value validation and bounds checking
- Robust exception management
- Defensive programming with internal assertions
- Accurate docstrings compliant with PEP257
- Static type annotations (`Optional`, `Any`) for modern editors and linters

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this code for both academic and commercial purposes.

---

## Acknowledgements

Developed with passion by Giuseppe Muschetta, M.Sc. in Computer Science.
Thanks to the powerful guidance of structured programming, academic methodology, and the pursuit of clarity and elegance in code.

