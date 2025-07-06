"""
main.py
========

Author: Giuseppe Muschetta
Email: g.muschetta@studenti.unipi.it
Project: DoublyLinkedList Data Structure in Python
Date: July 2025
University: University of Pisa – MSc in Computer Science,
                                 Specialization in "Data Science and Business Informatics"
Version: 1.0
License: MIT
GitHub: https://github.com/peppe212/Pythonic-LinkedList-Abstraction

Description:
    This main module serves as a full demonstration and testing suite
    for the DoublyLinkedList data structure implemented in Python. The
    goal is to validate every functional and auxiliary component of the
    list, including standard list operations, stack and queue behavior,
    data conversion, iterability, equality checks, magic methods, and
    advanced utilities like sorting and duplicate removal.

    All functionalities are tested programmatically and printed to
    standard output in a clear and organized format, making this script
    both a practical test suite and an educational showcase.

    This script is color-compatible in most Unix terminals.

"""

from doubly_linked_list import DoublyLinkedList

# Optional: colored terminal output for enhanced readability (Unix-compatible)
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

success = lambda msg: color(msg, '92')  # Green
error = lambda msg: color(msg, '91')    # Red
info = lambda msg: color(msg, '94')     # Blue

def main():
    """
    Main function to comprehensively test the DoublyLinkedList functionality.
    """
    print(info("=== STARTING COMPREHENSIVE DOUBLY LINKED LIST TEST SUITE ===\n"))

    print("This suite covers:")
    print(" 1. Initialization")
    print(" 2. Insertions (beginning/end/before/after)")
    print(" 3. Deletions (by value, by position)")
    print(" 4. Stack and Queue behavior")
    print(" 5. Cloning, Sorting, Duplicate Removal")
    print(" 6. Magic methods and iteration")
    print(" 7. Edge case and error management\n")
    print("=== STARTING COMPREHENSIVE DOUBLY LINKED LIST TEST SUITE ===")

    # --- Test Initialization and Empty State ---
    print("\n--- 1. Initialization and Empty State ---")
    dll = DoublyLinkedList()
    print(f"Initial list: {dll}")
    print(f"Size: {dll.get_size()}")
    print(f"Is empty?: {dll.is_empty()}")
    print(f"Python list conversion: {dll.to_python_list()}")
    assert dll.get_size() == 0 and dll.is_empty() and dll.to_python_list() == [], \
        "Initial state check failed."

    # --- Test insert_at_beginning ---
    print("\n--- 2. insert_at_beginning ---")
    dll.insert_at_beginning(10)
    print(f"After inserting 10: {dll} (Size: {dll.get_size()})")
    dll.insert_at_beginning(20)
    print(f"After inserting 20: {dll} (Size: {dll.get_size()})")
    dll.insert_at_beginning(30)
    print(f"After inserting 30: {dll} (Size: {dll.get_size()})")
    assert dll.to_python_list() == [30, 20, 10], "insert_at_beginning failed."
    try:
        dll.insert_at_beginning(None)
    except ValueError as e:
        print(f"Correctly caught error for inserting None at beginning: {e}")


    # --- Test insert_at_end ---
    print("\n--- 3. insert_at_end ---")
    dll.insert_at_end(5)
    print(f"After inserting 5: {dll} (Size: {dll.get_size()})")
    dll.insert_at_end(15)
    print(f"After inserting 15: {dll} (Size: {dll.get_size()})")
    assert dll.to_python_list() == [30, 20, 10, 5, 15], "insert_at_end failed."
    try:
        dll.insert_at_end(None)
    except ValueError as e:
        print(f"Correctly caught error for inserting None at end: {e}")

    # --- Test contains ---
    print("\n--- 4. contains ---")
    print(f"Does list contain 20? {dll.contains(20)}")
    print(f"Does list contain 100? {dll.contains(100)}")
    assert dll.contains(20) and not dll.contains(100), "contains failed."
    assert 20 in dll and not (100 in dll), "in operator (__contains__) failed."
    try:
        dll.contains(None)
    except ValueError as e:
        print(f"Correctly caught error for contains(None): {e}")


    # --- Test insert_after_node ---
    print("\n--- 5. insert_after_node ---")
    try:
        dll.insert_after_node(20, 25)
        print(f"After inserting 25 after 20: {dll} (Size: {dll.get_size()})")
        dll.insert_after_node(15, 1) # Insert after last node
        print(f"After inserting 1 after 15 (last): {dll} (Size: {dll.get_size()})")
        assert dll.to_python_list() == [30, 20, 25, 10, 5, 15, 1], "insert_after_node failed."
    except ValueError as e:
        print(f"Error during insert_after_node: {e}")
    try:
        dll.insert_after_node(99, 100) # Non-existent target
    except ValueError as e:
        print(f"Correctly caught error for inserting after non-existent node: {e}")
    try:
        dll.insert_after_node(20, None) # None as new_value
    except ValueError as e:
        print(f"Correctly caught error for inserting None value after node: {e}")


    # --- Test insert_before_node ---
    print("\n--- 6. insert_before_node ---")
    try:
        dll.insert_before_node(10, 8)
        print(f"After inserting 8 before 10: {dll} (Size: {dll.get_size()})")
        dll.insert_before_node(30, 35) # Insert before first node
        print(f"After inserting 35 before 30 (first): {dll} (Size: {dll.get_size()})")
        assert dll.to_python_list() == [35, 30, 20, 25, 8, 10, 5, 15, 1], "insert_before_node failed."
    except ValueError as e:
        print(f"Error during insert_before_node: {e}")
    try:
        dll.insert_before_node(99, 100) # Non-existent target
    except ValueError as e:
        print(f"Correctly caught error for inserting before non-existent node: {e}")
    try:
        dll.insert_before_node(20, None) # None as new_value
    except ValueError as e:
        print(f"Correctly caught error for inserting None value before node: {e}")


    # --- Test delete_at_beginning ---
    print("\n--- 7. delete_at_beginning ---")
    initial_size = dll.get_size()
    try:
        dll.delete_at_beginning()
        print(f"After deleting at beginning: {dll} (Size: {dll.get_size()})")
        assert dll.get_size() == initial_size - 1, "delete_at_beginning size check failed."
    except RuntimeError as e:
        print(f"Error during delete_at_beginning: {e}")
    try:
        empty_dll_test = DoublyLinkedList()
        empty_dll_test.delete_at_beginning()
    except RuntimeError as e:
        print(f"Correctly caught error for deleting from empty list (beginning): {e}")


    # --- Test delete_at_end ---
    print("\n--- 8. delete_at_end ---")
    initial_size = dll.get_size()
    try:
        dll.delete_at_end()
        print(f"After deleting at end: {dll} (Size: {dll.get_size()})")
        assert dll.get_size() == initial_size - 1, "delete_at_end size check failed."
    except RuntimeError as e:
        print(f"Error during delete_at_end: {e}")
    try:
        empty_dll_test = DoublyLinkedList()
        empty_dll_test.delete_at_end()
    except RuntimeError as e:
        print(f"Correctly caught error for deleting from empty list (end): {e}")


    # --- Test delete_value ---
    print("\n--- 9. delete_value ---")
    initial_size = dll.get_size()
    try:
        dll.delete_value(25)
        print(f"After deleting value 25: {dll} (Size: {dll.get_size()})")
        assert dll.get_size() == initial_size - 1 and not dll.contains(25), "delete_value failed."
        # Test deleting head value (current head is 30)
        dll.delete_value(30)
        print(f"After deleting value 30 (old head): {dll} (Size: {dll.get_size()})")
        # Test deleting tail value (current tail is 1)
        dll.delete_value(1)
        print(f"After deleting value 1 (old tail): {dll} (Size: {dll.get_size()})")
        assert not dll.contains(30) and not dll.contains(1), "delete_value for head/tail failed."
    except (ValueError, RuntimeError) as e:
        print(f"Error during delete_value: {e}")
    try:
        dll.delete_value(999) # Non-existent value
    except ValueError as e:
        print(f"Correctly caught error for deleting non-existent value: {e}")
    try:
        dll_empty_for_delete_val = DoublyLinkedList()
        dll_empty_for_delete_val.delete_value(1)
    except RuntimeError as e:
        print(f"Correctly caught error for deleting value from empty list: {e}")


    # --- Test delete_at_position ---
    print("\n--- 10. delete_at_position ---")
    dll.insert_at_beginning(100) # Re-add some elements for testing
    dll.insert_at_end(200)
    dll.insert_at_end(300)
    print(f"List before position deletion: {dll} (Size: {dll.get_size()})")
    initial_size = dll.get_size()
    try:
        dll.delete_at_position(0) # Delete head
        print(f"After deleting at position 0 (head): {dll} (Size: {dll.get_size()})")
        assert dll.get_size() == initial_size - 1, "delete_at_position (head) size check failed."
        initial_size = dll.get_size() # Update size
        dll.delete_at_position(dll.get_size() - 1) # Delete tail
        print(f"After deleting at last position (tail): {dll} (Size: {dll.get_size()})")
        assert dll.get_size() == initial_size - 1, "delete_at_position (tail) size check failed."
        initial_size = dll.get_size() # Update size
        if dll.get_size() > 1:
            dll.delete_at_position(1) # Delete middle element
            print(f"After deleting at position 1 (middle): {dll} (Size: {dll.get_size()})")
            assert dll.get_size() == initial_size - 1, "delete_at_position (middle) size check failed."
    except (ValueError, RuntimeError, IndexError, TypeError) as e:
        print(f"Error during delete_at_position: {e}")
    try:
        dll.delete_at_position(99) # Out of bounds
    except IndexError as e:
        print(f"Correctly caught error for deleting at out-of-bounds position: {e}")
    try:
        dll.delete_at_position(-1) # Negative index
    except IndexError as e:
        print(f"Correctly caught error for deleting at negative position: {e}")
    try:
        dll.delete_at_position("abc") # Invalid type
    except TypeError as e:
        print(f"Correctly caught error for deleting with non-integer position: {e}")
    try:
        dll_empty_pos = DoublyLinkedList()
        dll_empty_pos.delete_at_position(0) # Empty list
    except RuntimeError as e:
        print(f"Correctly caught error for deleting from empty list by position: {e}")


    # --- Test clear ---
    print("\n--- 11. clear ---")
    dll.clear()
    print(f"After clear(): {dll} (Size: {dll.get_size()})")
    assert dll.get_size() == 0 and dll.is_empty(), "clear failed."

    # --- Test reverse ---
    print("\n--- 12. reverse ---")
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    print(f"Original list for reverse: {dll}")
    try:
        dll.reverse()
        print(f"Reversed list: {dll}")
        assert dll.to_python_list() == [4, 3, 2, 1], "reverse failed."
    except RuntimeError as e:
        print(f"Error during reverse: {e}")
    try:
        empty_dll = DoublyLinkedList()
        empty_dll.reverse()
    except RuntimeError as e:
        print(f"Correctly caught error for reversing empty list: {e}")


    # --- Test clone ---
    print("\n--- 13. clone ---")
    cloned_dll = dll.clone()
    print(f"Original list: {dll}")
    print(f"Cloned list: {cloned_dll}")
    print(f"Are original and clone equal? {dll == cloned_dll}")
    dll.insert_at_end(5) # Modify original to ensure it's a deep copy
    print(f"Original after modification: {dll}")
    print(f"Cloned list (should be unchanged): {cloned_dll}")
    assert dll != cloned_dll and cloned_dll.to_python_list() == [4, 3, 2, 1], "clone failed."


    # --- Test sort ---
    print("\n--- 14. sort ---")
    sort_dll = DoublyLinkedList()
    sort_dll.insert_at_end(50)
    sort_dll.insert_at_end(10)
    sort_dll.insert_at_end(40)
    sort_dll.insert_at_end(20)
    sort_dll.insert_at_end(30)
    print(f"List before sorting: {sort_dll}")
    try:
        sort_dll.sort()
        print(f"List after ascending sort: {sort_dll}")
        assert sort_dll.to_python_list() == [10, 20, 30, 40, 50], "Ascending sort failed."
        sort_dll.sort(reverse=True)
        print(f"List after descending sort: {sort_dll}")
        assert sort_dll.to_python_list() == [50, 40, 30, 20, 10], "Descending sort failed."
    except (RuntimeError, TypeError) as e:
        print(f"Error during sort: {e}")
    try:
        empty_dll = DoublyLinkedList()
        empty_dll.sort()
    except RuntimeError as e:
        print(f"Correctly caught error for sorting empty list: {e}")
    try:
        unsortable_dll = DoublyLinkedList.from_python_list([1, 'b', 3])
        unsortable_dll.sort()
    except TypeError as e:
        print(f"Correctly caught error for sorting list with uncomparable types: {e}")


    # --- Test remove_duplicates ---
    print("\n--- 15. remove_duplicates ---")
    dup_dll = DoublyLinkedList()
    dup_dll.insert_at_end(1)
    dup_dll.insert_at_end(2)
    dup_dll.insert_at_end(1)
    dup_dll.insert_at_end(3)
    dup_dll.insert_at_end(2)
    dup_dll.insert_at_end(4)
    print(f"List before removing duplicates: {dup_dll}")
    try:
        dup_dll.remove_duplicates()
        print(f"List after removing duplicates: {dup_dll}")
        assert dup_dll.to_python_list() == [1, 2, 3, 4], "remove_duplicates failed."
    except RuntimeError as e:
        print(f"Error during remove_duplicates: {e}")
    try:
        empty_dll = DoublyLinkedList()
        empty_dll.remove_duplicates()
    except RuntimeError as e:
        print(f"Correctly caught error for removing duplicates from empty list: {e}")


    # --- Test Stack Methods (LIFO) ---
    print("\n--- 16. Stack Methods (LIFO) ---")
    stack_dll = DoublyLinkedList()
    print(f"Initial Stack: {stack_dll}")
    stack_dll.push("A")
    stack_dll.push("B")
    stack_dll.push("C")
    print(f"Stack after pushes: {stack_dll} (Size: {stack_dll.get_size()})")
    print(f"Peek stack: {stack_dll.peek()}")
    assert stack_dll.peek() == "C", "Stack peek failed."
    print(f"Pop stack: {stack_dll.pop()}")
    print(f"Stack after pop: {stack_dll} (Size: {stack_dll.get_size()})")
    assert stack_dll.to_python_list() == ["A", "B"] and stack_dll.get_size() == 2, "Stack pop failed."
    print(f"Pop stack: {stack_dll.pop()}")
    print(f"Pop stack: {stack_dll.pop()}")
    print(f"Stack after all pops: {stack_dll} (Size: {stack_dll.get_size()})")
    try:
        stack_dll.pop()
    except RuntimeError as e:
        print(f"Correctly caught error for popping from empty stack: {e}")
    try:
        stack_dll.peek()
    except RuntimeError as e:
        print(f"Correctly caught error for peeking into empty stack: {e}")
    stack_dll.push("X") # Add one element to test single element pop/peek
    print(f"Stack with one element: {stack_dll}")
    print(f"Pop single element: {stack_dll.pop()}")
    print(f"Stack after single element pop: {stack_dll}")
    assert stack_dll.is_empty(), "Single element stack pop failed."


    # --- Test Queue Methods (FIFO) ---
    print("\n--- 17. Queue Methods (FIFO) ---")
    queue_dll = DoublyLinkedList()
    print(f"Initial Queue: {queue_dll}")
    queue_dll.enqueue("First")
    queue_dll.enqueue("Second")
    queue_dll.enqueue("Third")
    print(f"Queue after enqueues: {queue_dll} (Size: {queue_dll.get_size()})")
    print(f"Peek front queue: {queue_dll.peek_front()}")
    assert queue_dll.peek_front() == "First", "Queue peek_front failed."
    print(f"Peek rear queue: {queue_dll.peek_rear()}")
    assert queue_dll.peek_rear() == "Third", "Queue peek_rear failed."
    print(f"Dequeue queue: {queue_dll.dequeue()}")
    print(f"Queue after dequeue: {queue_dll} (Size: {queue_dll.get_size()})")
    assert queue_dll.to_python_list() == ["Second", "Third"] and queue_dll.get_size() == 2, "Queue dequeue failed."
    print(f"Dequeue queue: {queue_dll.dequeue()}")
    print(f"Dequeue queue: {queue_dll.dequeue()}")
    print(f"Queue after all dequeues: {queue_dll} (Size: {queue_dll.get_size()})")
    try:
        queue_dll.dequeue()
    except RuntimeError as e:
        print(f"Correctly caught error for dequeue from empty queue: {e}")
    try:
        queue_dll.peek_front()
    except RuntimeError as e:
        print(f"Correctly caught error for peeking front into empty queue: {e}")
    try:
        queue_dll.peek_rear()
    except RuntimeError as e:
        print(f"Correctly caught error for peeking rear into empty queue: {e}")
    queue_dll.enqueue("Single") # Add one element to test single element dequeue/peek
    print(f"Queue with one element: {queue_dll}")
    print(f"Dequeue single element: {queue_dll.dequeue()}")
    print(f"Queue after single element dequeue: {queue_dll}")
    assert queue_dll.is_empty(), "Single element queue dequeue failed."


    # --- Test __eq__ ---
    print("\n--- 18. __eq__ ---")
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(2)
    list2.insert_at_end(1)
    list2.insert_at_end(2)
    list3 = DoublyLinkedList()
    list3.insert_at_end(1)
    list3.insert_at_end(3)
    list4 = DoublyLinkedList() # Empty

    print(f"List1: {list1}, List2: {list2}, List3: {list3}, List4: {list4}")
    print(f"List1 == List2? {list1 == list2}")
    print(f"List1 == List3? {list1 == list3}")
    print(f"List1 == List4? {list1 == list4}")
    print(f"List4 == empty list? {list4 == DoublyLinkedList()}")
    assert list1 == list2 and list1 != list3 and list1 != list4 and list4 == DoublyLinkedList(), "__eq__ failed."
    # Test equality with non-DoublyLinkedList object
    print(f"List1 == [1, 2]? {list1 == [1, 2]}")
    assert list1 != [1, 2], "__eq__ with non-DLL type failed."


    # --- Test __str__ and __repr__ ---
    print("\n--- 19. __str__ and __repr__ ---")
    test_list_repr = DoublyLinkedList()
    test_list_repr.insert_at_end("hello")
    test_list_repr.insert_at_end("world")
    print(f"__str__ representation: {test_list_repr}")
    print(f"__repr__ representation: {repr(test_list_repr)}")
    assert str(test_list_repr) == "['hello', 'world']", "__str__ failed."
    assert repr(test_list_repr) == "DoublyLinkedList(size=2)", "__repr__ failed."


    # --- Test __iter__ ---
    print("\n--- 20. __iter__ ---")
    iter_dll = DoublyLinkedList()
    iter_dll.insert_at_end("A")
    iter_dll.insert_at_end("B")
    iter_dll.insert_at_end("C")
    print("Iterating through list (forward):")
    iterated_elements = []
    for item in iter_dll:
        print(f"  Visited: {item}")
        iterated_elements.append(item)
    assert iterated_elements == ["A", "B", "C"], "__iter__ failed."


    # --- Test __reversed__ ---
    print("\n--- 21. __reversed__ ---")
    reversed_elements = []
    print("Iterating through list (reversed):")
    for item in reversed(iter_dll):
        print(f"  Visited (reversed): {item}")
        reversed_elements.append(item)
    assert reversed_elements == ["C", "B", "A"], "__reversed__ failed."
    try:
        empty_dll = DoublyLinkedList()
        for item in reversed(empty_dll):
            pass # Should not raise error, just yield nothing
        print("Reversed on empty list yields nothing (correct).")
    except Exception as e:
        print(f"Error for reversed on empty list: {e}")


    # --- Test __getitem__ (indexing) ---
    print("\n--- 22. __getitem__ ---")
    getitem_dll = DoublyLinkedList.from_python_list([10, 20, 30, 40, 50])
    print(f"List for getitem: {getitem_dll}")
    print(f"Element at index 0: {getitem_dll[0]}")
    print(f"Element at index 2: {getitem_dll[2]}")
    print(f"Element at last index ({len(getitem_dll)-1}): {getitem_dll[len(getitem_dll)-1]}")
    assert getitem_dll[0] == 10 and getitem_dll[2] == 30 and getitem_dll[len(getitem_dll)-1] == 50, "__getitem__ failed."
    try:
        print(f"Element at index 99: {getitem_dll[99]}") # Out of bounds
    except IndexError as e:
        print(f"Correctly caught error for __getitem__ out of bounds: {e}")
    try:
        print(f"Element at index -1: {getitem_dll[-1]}") # Negative index
    except IndexError as e:
        print(f"Correctly caught error for __getitem__ negative index: {e}") # Your _get_node_at_position throws IndexError directly
    try:
        print(f"Element at index 'a': {getitem_dll['a']}") # Invalid type
    except TypeError as e:
        print(f"Correctly caught error for __getitem__ invalid type: {e}")
    try:
        empty_dll = DoublyLinkedList()
        var = empty_dll[0]  # Access empty list
    except IndexError as e:
        print(f"Correctly caught error for __getitem__ on empty list: {e}")


    # --- Test __setitem__ (assignment by index) ---
    print("\n--- 23. __setitem__ ---")
    setitem_dll = DoublyLinkedList.from_python_list(['a', 'b', 'c', 'd'])
    print(f"List for setitem: {setitem_dll}")
    setitem_dll[0] = 'first'
    setitem_dll[2] = 'middle'
    setitem_dll[len(setitem_dll)-1] = 'last'
    print(f"List after assignments: {setitem_dll}")
    assert setitem_dll.to_python_list() == ['first', 'b', 'middle', 'last'], "__setitem__ failed."
    try:
        setitem_dll[99] = 'error' # Out of bounds
    except IndexError as e:
        print(f"Correctly caught error for __setitem__ out of bounds: {e}")
    try:
        setitem_dll[-1] = 'error' # Negative index
    except IndexError as e:
        print(f"Correctly caught error for __setitem__ negative index: {e}")
    try:
        setitem_dll['a'] = 'error' # Invalid type
    except TypeError as e:
        print(f"Correctly caught error for __setitem__ invalid type: {e}")
    try:
        setitem_dll[0] = None # Set None value
    except ValueError as e:
        print(f"Correctly caught error for __setitem__ with None value: {e}")
    try:
        empty_dll = DoublyLinkedList()
        empty_dll[0] = 'value' # Assign to empty list
    except IndexError as e:
        print(f"Correctly caught error for __setitem__ on empty list: {e}")


    print("\n=== ALL DOUBLY LINKED LIST TESTS COMPLETED SUCCESSFULLY! ===")


if __name__ == '__main__':
    main()
