"""
Implementation of a linked list
6/1/2021
@author Usman Naveed
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, head_node):
        self.head = head_node

    # add to front
    def add_to_front(self, node_obj):
        tmp = self.head
        self.head = node_obj
        self.head.next = tmp

    # add to back of the linked list
    def add_to_back(self, node_obj):
        curr_node = self.head
        end_of_list = False
        while end_of_list is False:
            if curr_node.next is None:
                curr_node.next = node_obj
                end_of_list = True
            else:
                curr_node = curr_node.next

    # remove item from front
    def remove_first_node(self):
        if self.head is None:
            return "The list is already empty, nothing to remove"
        elif self.head.next is None:
            self.head = None
            return "Your list is now empty"
        else:
            next_node = self.head.next
            self.head = next_node

    # remove item from the back
    def remove_last_node(self):
        if self.head is None:
            return "The list is already empty, nothing to remove"
        elif self.head.next is None:
            self.head = None
            return "Your list is now empty "
        else:
            curr_node = self.head
            prev_node = None
            is_end = False
            while is_end is False:
                if curr_node.next is None:
                    prev_node.next = None
                    is_end = True
                else:
                    prev_node = curr_node
                    curr_node = curr_node.next

    # check if a value is present in the list
    def is_present(self, value):
        curr = self.head
        while curr.next is not None:
            if curr.val == value:
                return True
            else:
                curr = curr.next
        return False

    def __str__(self):
        vals = []  # initializing the vals array to hold all the values of the linked list
        curr = self.head
        while curr is not None:
            vals.append(curr.val)  # append the value of the node to the val array
            curr = curr.next  # move the head pointer to the next node to continue traverse
        st = [str(x) for x in vals]  # convert each value to a string so we can join it with the arrow
        return " -> ".join(st)
