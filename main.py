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


def build_tree(path: str) -> Node:
    parent_root = Node(path, True)
    current_root = parent_root

    for path, is_dir in read_dir(path):
        node = Node(path, is_dir)
        dir_path = os.path.dirname(node.path)
        back_dirs = current_root.path.replace(dir_path, '')
        back_times = len(back_dirs.split(os.sep)) - 1
        while back_times > 0 and current_root.parent:
            back_times -= 1
            current_root = current_root.parent

        current_root.add_node(node)

        if is_dir:
            current_root = node

    return parent_root


def print_tree(node: Node, level: int=0):
    file_name = os.path.basename(node.path)
    spaces = '  ' * level
    print(f'{spaces}{file_name}')
    for child in node.children:
        print_tree(child, level + 1)


if __name__ == '__main__':
    root_dir = os.path.dirname(__file__)
    # print(*read_dir(root_dir))
    tree = build_tree(root_dir)
    print_tree(tree)


# first = r'D:\directory-tree\.git\refs\tags', True
# # second = r'D:\directory-tree\.gitignore', False
# # dir_path = os.path.dirname(second[0]) + os.sep
# # back_dirs = first[0].replace(dir_path, '')
# # back_times = len(back_dirs.split(os.sep))
# #
# # new_first = first[0].split(os.sep)
# # new_second = second[0].split(os.sep)
#
# # print(new_first)
# # print(new_second)
# #
# # print(len(new_first) - len(new_second) + first[1])
#
# # print(back_dirs)
# # print(dir_path)
# # print(back_times)
