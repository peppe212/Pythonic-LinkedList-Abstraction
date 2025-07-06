"""
Doubly Linked List Module (Main Class)

Author: Giuseppe Muschetta
Email: g.muschetta@studenti.unipi.it
Date: July 2025
University: University of Pisa – MSc in Computer Science,
                                 Specialization in "Data Science and Business Informatics"

Description:
-------------
This module defines the `DoublyLinkedList` class, which implements a dynamic,
bidirectional list structure supporting efficient insertions and deletions at both ends
as well as arbitrary positions.

The class provides:
    - Core operations: insertions, deletions, traversal.
    - Extended utilities: reversal, clearing, searching, deep cloning, sorting, duplicate removal.
    - Interface flexibility: support for Pythonic constructs such as iteration (`__iter__`),
      indexing (`__getitem__`, `__setitem__`), equality checks (`__eq__`), and built-in functions
      like `len()` and `str()`.

This implementation is modularized for clarity and maintainability,
with the `Node` class defined separately in `node.py`.

Compatibility:
    - Python 3.10+

Usage:
    - Intended for educational and academic use within structured data manipulation.
    - Easily extendable for stacks, queues, and higher-level data abstractions.
"""


# Import the Node class from the node module
from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    # Metodi Ausiliari
    @staticmethod
    def _validate_value(value):
        if value is None:
            raise ValueError("Cannot insert None into the list.")

    def _get_node_at_position(self, position):
        """
        Retrieves the node located at a specified zero-based position in the list.

        The traversal is optimized: it starts from the head if the position is in
        the first half of the list, or from the tail otherwise.

        Parameters:
            position (int): The index of the node to retrieve.

        Returns:
            Node: The node at the given index.

        Raises:
            TypeError: If the position is not an integer.
            IndexError: If the position is out of bounds.
        """
        if not isinstance(position, int):
            raise TypeError("Position must be an integer.")

        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self.size}.")

        current = self.head
        # Optimized traversal: if position is in the latter half, traverse from tail
        if position > self.size // 2:
            current = self.tail
            for _ in range(self.size - 1, position, -1):
                current = current.prev
        else:
            for _ in range(position):
                current = current.next

        assert current is not None, "Internal error: Node not found at valid positive position after traversal."
        return current


    def clear(self):
        """
        Removes all elements from the list by resetting head, tail, and size.

        This method does not explicitly delete individual nodes, relying on Python's
        garbage collector to reclaim memory.

        Returns:
            None
        """
        self.head = None
        self.tail = None
        self.size = 0
        assert self.head is None and self.tail is None and self.size == 0, \
            "Internal error: List not properly cleared."


    def insert_at_beginning(self, value):
        """
        Inserts a new node containing the given value at the beginning of the list.

        This method modifies the head of the list, and properly updates the previous
        links and tail if necessary.

        Parameters:
            value: The value to be inserted into the list.

        Returns:
            None

        Raises:
            ValueError: If the provided value is None.
        """
        self._validate_value(value)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return


    def insert_at_end(self, value):
        """
        Inserts a new node containing the given value at the end of the list.

        If the list is empty, the new node becomes both the head and tail.
        Otherwise, it is appended after the current tail.

        Parameters:
            value: The value to be inserted into the list.

        Returns:
            None

        Raises:
            ValueError: If the provided value is None.
        """
        self._validate_value(value)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return


    def insert_after_node(self, target_value, new_value):
        """
        Inserts a new node with a given value immediately after the node
        containing the target value.

        Parameters:
            target_value: The value of the node before which the new node is to be inserted.
            new_value: The value to be inserted.

        Returns:
            None

        Raises:
            ValueError: If the target value is not found or any of the values are None.
        """
        self._validate_value(target_value)
        self._validate_value(new_value)
        if not self.contains(target_value):
            raise ValueError(f"{target_value} has not been found in the list")
        # Raggiungiamo il nodo contenente il target_value
        current = self.head
        on_target = False
        while current and not on_target:
            if current.info == target_value:
                on_target = True
            else:
                current = current.next
        # Creo il nuovo nodo
        new_node = Node(new_value)
        # Se target_value è l'ultimo nodo della lista
        if current.next is None:
            assert (current == self.tail)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            assert (current.next is not None)
            new_node.next = current.next
            current.next.prev = new_node
            new_node.prev = current
            current.next = new_node
        self.size += 1
        return


    def contains(self, value) -> bool:
        """
        Checks whether the specified value exists in the list.

        Iterates through the list starting from the head to determine whether
        any node contains the specified value.

        Parameters:
            value: The value to be searched in the list.

        Returns:
            bool: True if the value is found in the list, False otherwise.

        Raises:
            ValueError: If the provided value is None.
        """
        self._validate_value(value)

        current = self.head
        found = False
        while current and not found:
            if current.info == value:
                found = True
            else:
                current = current.next
        return found


    def insert_before_node(self, target_value, new_value):
        """
        Inserts a new node with a given value immediately before the node
        containing the target value.

        Parameters:
            target_value: The value of the node before which the new node is to be inserted.
            new_value: The value to be inserted.

        Returns:
            None

        Raises:
            ValueError: If the target value is not found or any of the values are None.
        """
        self._validate_value(target_value)
        self._validate_value(new_value)
        if not self.contains(target_value):
            raise ValueError(f"{target_value} has not been found in the list")
        # Raggiungiamo il nodo contenente il target_value
        current = self.head
        on_target = False
        while current and not on_target:
            if current.info == target_value:
                on_target = True
            else:
                current = current.next
        # Creo il nuovo nodo
        new_node = Node(new_value)
        # Se target_value è il primo nodo della lista
        if current.prev is None:
            assert (current == self.head)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            assert (current.prev is not None)
            current.prev.next = new_node
            new_node.prev = current.prev
            new_node.next = current
            current.prev = new_node
        self.size += 1
        return


    def delete_at_beginning(self):
        """
        Removes the first element (head) from the list.

        Adjusts the head pointer to the next node and updates the size
        accordingly. If the list contains only one element, both head and tail
        are set to None.

        Returns:
            None

        Raises:
            RuntimeError: If the list is empty.
        """
        if self.head is None or self.size == 0:
            raise RuntimeError("List must contain at least 1 value")

        if self.get_size() == 1:
            self.head = self.head.next  #e quindi va a None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return


    def delete_at_end(self):
        """
        Removes the last element (tail) from the list.

        Adjusts the tail pointer to the previous node and updates the size.
        If the list has only one element, both head and tail are set to None.

        Returns:
            None

        Raises:
            RuntimeError: If the list is empty.
        """
        if self.head is None or self.tail is None or self.size == 0:
            raise RuntimeError("List must contain at least 1 value")
    
        if self.get_size() == 1:
            self.head = self.head.next  #e quindi va a None
            self.tail = None
        # Se la lista contiene più di 1 elemento, quindi da 2 elementi in poi
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        # aggiorno size
        self.size -= 1
        return

    def delete_value(self, value):
        """
        Deletes the first occurrence of the specified value from the list.

        Adjusts the previous and next pointers of neighboring nodes to maintain
        list integrity after the removal.

        Parameters:
            value: The value to be removed from the list.

        Returns:
            None

        Raises:
            ValueError: If the value does not exist in the list or is None.
            RuntimeError: If the list is empty.
        """
        self._validate_value(value)
        if self.head is None:
            raise RuntimeError("List must not be empty to delete a specific value.")

        current = self.head
        found = False
        while current and not found:
            if current.info == value:
                found = True
            else:
                current = current.next

        if not found:
            raise ValueError(f"'{value}' does not exist in the list.")

        if current.prev is None:  # This means 'current' is the head
            self.delete_at_beginning()  # This already handles self.size -= 1
        elif current.next is None:  # This means 'current' is the tail
            self.delete_at_end()  # This already handles self.size -= 1
        else:  # 'current' is a middle node
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1


    def delete_at_position(self, position):
        """
        Deletes the element at the specified position.
        # ... (docstring invariato)
        """
        if self.head is None or self.size == 0:
            raise RuntimeError("List must contain at least 1 value to delete by position.")

        # _get_node_at_position will now correctly handle out-of-bounds positions
        # with IndexError, since we've already handled the empty list case.
        current = self._get_node_at_position(position)

        if current.prev is None:
            self.delete_at_beginning()
        elif current.next is None:
            self.delete_at_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1


    def get_size(self) -> int:
        """
        Retrieves the number of elements currently stored in the list.

        Returns:
            int: The number of nodes in the list.
        """
        return self.size


    def is_empty(self) -> bool:
        """
        Checks whether the list is empty.

        Returns:
            bool: True if the list contains no elements, False otherwise.
        """
        return self.size == 0


    def to_python_list(self) -> list:
        """
        Converts the entire doubly linked list into a standard Python list.

        Returns a list containing the same elements in the same order.

        Returns:
            list: A new list containing the values of the linked list.

        Note:
            If the list is empty, an empty list is returned.
        """
        if self.head is None or self.tail is None or self.size == 0:
            return []

        pythonic_list = []
        current = self.head
        while current:
            pythonic_list.append(current.info)
            current = current.next

        assert (type(pythonic_list) is list)
        return pythonic_list


    @staticmethod
    def from_python_list(python_list: list) -> "DoublyLinkedList":
        """
        Creates a new DoublyLinkedList instance by copying all elements
        from a standard Python list, preserving their original order.

        Parameters:
            python_list (list): The input Python list containing the elements
                                to be inserted into the new doubly linked list.

        Returns:
            DoublyLinkedList: A new list populated with the elements from the
                              provided Python list.

        Raises:
            ValueError: If the input is not a valid Python list.
        """
        if not isinstance(python_list, list):
            raise TypeError("Input must be a standard Python list.")

        dll = DoublyLinkedList()
        for item in python_list:
            dll.insert_at_end(item)

        return dll



    def reverse(self):
        """
        Reverses the entire doubly linked list in place.

        This method inverts the direction of the list by swapping the `next`
        and `prev` pointers for each node, effectively reversing the traversal
        order. After all pointers are reversed, the `head` and `tail` references
        are also swapped to maintain structural integrity.

        This operation is performed in linear time \(\mathcal{O}(n)\), where \(n\)
        is the number of elements in the list, and it does not allocate additional memory.

        Returns:
            None

        Raises:
            RuntimeError: If the list is empty.
        """
        if self.head is None or self.tail is None or self.size == 0:
            raise RuntimeError("List must not be empty")
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev

        temp_final = self.head
        self.head = self.tail
        self.tail = temp_final
        return

    def clone(self) -> "DoublyLinkedList":
        """
        Creates and returns a deep copy of the current list,
        replicating all nodes and values in the same order.

        Returns:
            DoublyLinkedList: A new instance containing a deep copy
            of all elements from the original list.
        """
        clone_to_return = DoublyLinkedList()
        if self.head is None or self.tail is None or self.size == 0:
            return clone_to_return
        current = self.head
        while current:
            clone_to_return.insert_at_end(current.info)
            current = current.next
        return clone_to_return


    def sort(self, reverse: bool = False) -> None:
        """
        Sorts the elements of the list in ascending order by default,
        or in descending order if reverse=True. This method uses Python's
        built-in sorting for optimal performance and reinserts the values
        into the list in sorted order.

        Parameters:
            reverse (bool): If set to True, the list is sorted in descending order.
                            Defaults to False (ascending sort).

        Returns:
            None
        """
        if self.head is None or self.tail is None or self.size == 0:
            print("Cannot sort: list is empty.")
            return

        python_list = self.to_python_list()
        try:
            python_list.sort(reverse=reverse)
        except TypeError:
            print("Cannot sort: the list contains elements that cannot be compared with each other.")
            return

        self.clear()
        for item in python_list:
            self.insert_at_end(item)
        print("List sorted successfully." if not reverse else "List sorted in reverse order.")
        return


    def remove_duplicates(self) -> None:
        """
        Removes all duplicate elements from the list, preserving only the first
        occurrence of each value. The order of remaining elements is preserved.

        Parameters: None

        Returns: None
        """
        if self.head is None or self.tail is None or self.size == 0:
            raise RuntimeError("List must not be empty")
        python_list = self.to_python_list()
        # creo un insieme chiamato seen
        seen = set()
        result = []
        for item in python_list:
            if item not in seen:
                seen.add(item)
                result.append(item)

        self.clear()
        for item in result:
            self.insert_at_end(item)
        return


    # STACK METHODS (LIFO)
    # This means you can use this DoublyLinkedList as a Stack
    def push(self, value) -> None:
        """
        Pushes a new element onto the top of the stack (end of the list).

        Parameters:
            value: The value to be inserted into the list.

        Returns:
            None

        Raises:
            ValueError: If the provided value is None.
        """
        self.insert_at_end(value)
        return


    def pop(self):
        """
        Removes and returns the top (last) element of the stack (end of the list).

        Returns:
            The value of the element that was removed.

        Raises:
            RuntimeError: If the list (stack) is empty.
        """
        if not self.head or not self.tail or self.size == 0:
            raise RuntimeError("Stack must not be empty")
        if self.size == 1:
            value = self.head.info
            assert(value == self.tail.info)
            self.clear() # ci pensa la clear e resettare anche size
            return value
        else:
            value = self.tail.info
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return value


    def peek(self):
        """
        Returns (without removing) the value of the top (last) element of the stack.

        Returns:
            The value of the last element in the list.

        Raises:
            RuntimeError: If the list (stack) is empty.
        """
        if not self.head or not self.tail or self.size == 0:
            raise RuntimeError("Stack must not be empty")
        value = self.tail.info
        return value


    # QUEUE METHODS (FIFO)
    # This means you can use this DoublyLinkedList as a Queue
    def enqueue(self, value) -> None:
        """
        Inserts an element at the end of the queue (tail of the list).

        Parameters:
            value: The value to be enqueued.

        Returns:
            None

        Raises:
            ValueError: If the provided value is None.
        """
        self.insert_at_end(value)
        return


    def dequeue(self):
        """
        Removes and returns the front (first) element of the queue (head of the list).

        Returns:
            The value of the dequeued element.

        Raises:
            RuntimeError: If the queue (list) is empty.
        """
        if not self.head or not self.tail or self.size == 0:
            raise RuntimeError("Queue must not be empty")
        value = self.head.info
        if self.size == 1:
            self.clear()  # This sets self.size = 0
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1  # <--- MOVE IT HERE
        # REMOVE self.size -= 1 from here
        return value




    def peek_front(self):
        """
        Returns (without removing) the front (first) element of the queue.

        Returns:
            The value of the first element in the list.

        Raises:
            RuntimeError: If the queue (list) is empty.
        """
        if not self.head or not self.tail or self.size == 0:
            raise RuntimeError("Queue must not be empty")
        return self.head.info


    def peek_rear(self):
        """
        Returns (without removing) the rear (last) element of the queue.

        Returns:
            The value of the last element in the list.

        Raises:
            RuntimeError: If the queue (list) is empty.
        """
        if not self.head or not self.tail or self.size == 0:
            raise RuntimeError("Queue must not be empty")
        return self.tail.info


    def __eq__(self, other) -> bool:
        """
            Compares this list with another DoublyLinkedList for equality.
            Two lists are considered equal if they have the same size and
            contain the same elements in the same order.

            Parameters:
                other (DoublyLinkedList): The list to compare with.

            Returns:
                bool: True if both lists are equal, False otherwise.
            """
        if not isinstance(other, DoublyLinkedList):
            return False

        if self.size != other.size:
            return False

        current_self = self.head
        current_other = other.head

        while current_self and current_other:
            if current_self.info != current_other.info:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True


    def __str__(self):
        """
        Returns a human-readable string representation of the list content,
        showing elements in forward order as a native Python list.

        Returns:
            str: The list content as a string.
        """
        return str(self.to_python_list())

    def __repr__(self):
        """
        Returns a detailed representation of the DoublyLinkedList object,
        useful for debugging and development purposes.

        Returns:
            str: A string showing the type and size of the list.
        """
        return f"DoublyLinkedList(size={self.size})"


    def __iter__(self):
        """
        Returns an iterator over the elements in the doubly linked list,
        enabling support for iteration using the `for` loop and other
        iterable-based constructs in Python.

        This method starts from the head of the list and yields each element's
        value in forward order, one by one, without modifying the original structure.

        Returns:
            Iterator: An iterator that sequentially yields the values stored
                      in the nodes from head to tail.

        Raises:
            None
        """
        current = self.head
        while current:
            yield current.info
            current = current.next


    def __reversed__(self):
        """
        Returns a reverse iterator over the elements in the doubly linked list,
        allowing the use of the built-in `reversed()` function without modifying
        the original list.

        This method provides a clean and memory-efficient way to iterate over the
        elements in reverse order, starting from the tail and moving backward.

        Returns:
            Iterator: An iterator yielding elements in reverse order.

        Raises:
            None
        """
        current = self.tail
        while current:
            yield current.info
            current = current.prev


    def __setitem__(self, index: int, value):
        """
        Replaces the element at the specified index with a new value using bracket notation (e.g., dll[index] = value).

        Parameters:
            index (int): The zero-based position where the value should be updated.
            value: The new value to assign at the given index.

        Returns:
            None

        Raises:
            TypeError: If the index is not an integer.
            IndexError: If the index is out of the valid range (either positive or negative).
            ValueError: If the provided value is None (optional but recommended for data integrity).
        """
        self._validate_value(value)
        if not isinstance(index, int):
            raise TypeError(f"{index} must be an integer")
        if index < 0:
            positive_index = index + self.size
            if positive_index < 0:
                raise IndexError(f"{index} is out of bounds")
        else:
            positive_index = index
            if positive_index >= self.size:
                raise IndexError(f"{index} is out of bounds")
        node = self._get_node_at_position(positive_index)
        node.info = value
        return



    def __getitem__(self, index: int):
        """
        Retrieves the element at the specified index using bracket notation (e.g., dll[index]).

        Parameters:
            index (int): The zero-based index of the element to retrieve.

        Returns:
            The value stored at the given index.

        Raises:
            TypeError: If the index is not an integer.
            IndexError: If the index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError(f"{index} must be an integer")
        if index < 0:
            positive_index = index + self.size
            if positive_index < 0:
                raise IndexError(f"{index} is out of bounds")
        else:
            positive_index = index
            if positive_index >= self.size:
                raise IndexError(f"{index} is out of bounds")
        node = self._get_node_at_position(positive_index)
        return node.info

    def __len__(self) -> int:
        """
        Returns the number of elements currently stored in the list.

        This method enables the use of the built-in len() function on the
        DoublyLinkedList instance, returning the current size of the list.

        Returns:
            int: The number of nodes (elements) present in the list.

        Raises:
            None
        """
        return self.size


    def __contains__(self, value) -> bool:
        """
        Checks whether the specified value exists within the doubly linked list.

        This method enables support for the `in` keyword in Python expressions
        (e.g., `if value in dll:`), improving code readability and conciseness.

        Parameters:
            value: The element to be searched within the list.

        Returns:
            bool: True if the value exists in the list, False otherwise.

        Raises:
            ValueError: If the provided value is None.
        """
        return self.contains(value)


