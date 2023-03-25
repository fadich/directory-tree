import os
from typing import List, Optional


def read_dir(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            yield file_path, True
            yield from read_dir(file_path)
        else:
            yield file_path, False


class Node:

    def __init__(self, path: str, is_dir: bool):
        self.path = path
        self.is_dir = is_dir
        self.children: List[Node] = []
        self.parent: Optional[Node] = None

    def add_node(self, node: 'Node'):
        self.children.append(node)
        node.parent = self


if __name__ == '__main__':
    root_dir = os.path.dirname(__file__)
    # print(*read_dir(root_dir))
    parent_root = Node(root_dir, True)
    current_root = parent_root

    for path, is_dir in read_dir(root_dir):
        node = Node(path, is_dir)
        current_root.add_node(node)
        root_split = current_root.path.split(os.sep)
        node_split = node.path.split(os.sep)
        len_split = len(root_split) - len(node_split)
        while len_split:
            len_split -= 1
            current_root = current_root.parent

        if is_dir:
            current_root = node
        print(path, is_dir)


first = r'D:\directory-tree\.git\refs\tags', True
second = r'D:\directory-tree\.gitignore', False

new_first = first[0].split(os.sep)
new_second = second[0].split(os.sep)

print(new_first)
print(new_second)

print(len(new_first) - len(new_second) + first[1])


