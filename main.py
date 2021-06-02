from data_structures.LinkedList import Node, LinkedList
from data_structures.StacksandQueues import Stack, Queue

first_item = Node(5)
second_item = Node(55)

stack = Stack(first_item)
stack.add(second_item)
stack.add(Node(66))
print(stack)
stack.pop()
print(stack)
queue = Queue(Node(86))
queue.add(Node(4444))
queue.add(Node(99))
print(queue)
queue.remove()
print(queue)





























# testing out the linked list class
'''
first_node = Node(5)
second_node = Node(67)
third_node = Node(6)
linked_list = LinkedList(first_node)
linked_list.add_to_front(second_node)
linked_list.add_to_front(third_node)
print(linked_list)
linked_list.remove_last_node()
print(linked_list)
linked_list.remove_last_node()
print(linked_list)
linked_list.remove_last_node()
print(linked_list)
linked_list.add_to_front(second_node)
linked_list.add_to_front(third_node)
print(linked_list)
linked_list.remove_first_node()
print(linked_list)
linked_list.remove_first_node()
print(linked_list)
print(linked_list.remove_first_node())
'''

