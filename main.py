import os


def read_dir(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            yield file_path, True
            yield from read_dir(file_path)
        else:
            yield file_path, False


root_dir = os.path.dirname(__file__)
print(*read_dir(root_dir))
