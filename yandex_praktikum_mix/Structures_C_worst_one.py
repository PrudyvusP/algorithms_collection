class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node: Node, idx: int) -> Node:

    if idx == 0:
        return get_node_by_index(node, idx + 1)

    previous_node = get_node_by_index(node, idx - 1)
    node_to_del = get_node_by_index(node, idx)
    previous_node.next_item = node_to_del.next_item
    return node


def print_node(node) -> None:
    while node:
        print(node.value)
        node = node.next_item


"""
if __name__ == '__main__':
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_node = solution(node0, 0)
    print_node(new_node)
"""

