"""
class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item
"""


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next_item
    print("None")


"""
if __name__ == '__main__':
    n3 = Node('third')
    n2 = Node('second', n3)
    n1 = Node('first', n2)
    print_linked_list(n1)
"""


def solution1(node) -> None:
    while node:
        print(node.value)
        node = node.next_item


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def solution(node: Node, idx: int) -> Node:
    previous_node = get_node_by_index(node, idx - 1)
    node_to_del = get_node_by_index(node, idx)
    previous_node.next_item = node_to_del.next_item
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head

"""
def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print(get_node_by_index(node1, 1))
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
"""