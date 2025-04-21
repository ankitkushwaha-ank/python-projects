class Node:
    def __init__(self.data):
    self.data = data
    self.next = none

    def traverse_print(head):
        currentNode = head
        while (currentNode.data , end="-->"):
            currentNode = currentNode.next


print("None")

node1 = Node(2021)
node2 = Node(2022)
node3 = Node(2023)
node4 = Node(2024)

node1.next = node2
node2.next = node3
node3.next = node4


# Deletion of Singly Linked List
#1. Deletion at the Beginning of singly linked list
# Function to remove the first node

def remove_first(head):
    if not head:
        return None

    temp = head
    head = head.next
    temp = None  # Optional: Explicitly set temp to None for clarity/garbage collection

    return head

# Call of removal function
head = remove_first(node1)  # Assuming node1 is the initial head of the list

traverse_print(head)      # Assuming traverse_print is a function to print the list

# Deletion at the End of Singly Linked List
# Traverse the list to find the second to last node

def remove_last(head):
    if head is None:
        return None

    # if the list has only one node
    if head.next is None:
        head = None
        return None

    # find the second last node

    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next

    second_last.next = None
    return head

    # Call above function

    head = remove_last(node1)  # Assuming node1 is the head of your list
    traverse_print(head)  # Assuming traverse_print is a function to print the list

# Deletion at a specific position of singly linked list
# function to delete a node at a specific position

def delete_position(head, position):
    # if the list is empty
    if head is None or position < 1:
        return head

    # if the head needs to be deleted
    if position == 1:
        temp = head
        head = head.next
        temp = None  # Good practice: Explicitly deallocate
        return head

    # Traverse to the node before the position to be deleted
    current = head
    for i in range(1, position - 1):
        if current is None or current.next is None:  # Handle invalid positions
            return head  # Or raise an exception: raise IndexError("Position out of range")
        current = current.next

    # if the list is empty
    if head is None or position < 1:
        return head

    # if the head needs to be deleted
    if position == 1:
        temp = head
        head = head.next
        temp = None  # Good practice: Explicitly deallocate
        return head

    # Traverse to the node before the position to be deleted
    current = head
    for i in range(1, position - 1):
        if current is not None:  # Check if current is valid before moving
            current = current.next

    def delete_position(head, position):
        if head is None or position < 1:
            return head

        if position == 1:
            temp = head
            head = head.next
            temp = None
            return head

        current = head
        for i in range(1, position - 1):
            if current is None or current.next is None:
                return head  # Or raise IndexError("Position out of range")
            current = current.next

        if current is None or current.next is None:
            return head  # Or raise IndexError("Position out of range")

        temp = current.next  # The code from your image starts here
        current.next = current.next.next
        temp = None
        return head