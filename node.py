"""
node.py
========

Author: Giuseppe Muschetta
Email: g.muschetta@studenti.unipi.it
Project: DoublyLinkedList Data Structure in Python
Date: July 2025
University: University of Pisa – MSc in Computer Science,
                                 Specialization in "Data Science and Business Informatics"
Version: 1.0
License: MIT
GitHub: https://github.com/gmuschetta/doubly-linked-list

Description:
-------------
This module defines the `Node` class used as the core building block
of the DoublyLinkedList data structure. Each node stores a single value
along with references to both the next and previous nodes in the sequence.

The design supports bidirectional traversal, enabling efficient operations
such as insertion and deletion at both ends and at arbitrary positions.

Note:
    This class is intended for internal use within the DoublyLinkedList
    and should not be accessed directly outside the list context.
"""

from typing import Any, Optional

class Node:
    """
    Represents a single node in a doubly linked list.

    Attributes:
        info (Any): The value stored in the node.
        next (Optional[Node]): Reference to the next node (or None).
        prev (Optional[Node]): Reference to the previous node (or None).
    """

    def __init__(self, info: Any):
        """
        Initializes a new Node with the specified value.

        Parameters:
            info (Any): The data value to be stored in the node.
        """
        self.info = info
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None

    def __repr__(self):
        """
        Returns a concise representation of the node for debugging purposes.

        Returns:
            str: A string representation of the node value.
        """
        return f"Node({repr(self.info)})"
