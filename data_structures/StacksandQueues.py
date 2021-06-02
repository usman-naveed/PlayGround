from data_structures.LinkedList import LinkedList


# gotta love OOP

class Stack(LinkedList):

    def pop(self):
        return super().remove_first_node()

    def add(self, node):
        return super().add_to_front(node)


class Queue(LinkedList):

    def remove(self):
        return super().remove_last_node()

    def add(self, node):
        return super().add_to_front(node)
