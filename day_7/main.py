from anytree import Node, RenderTree


def remove_ls_commands(terminal_output: list[str]) -> list[str]:
    return list(filter(lambda line: line != '$ ls', terminal_output))


def read_input(input_path: str) -> list[str]:
    with open(input_path, 'r') as input_file:
        terminal_output = remove_ls_commands(input_file.read().split('\n'))
    return terminal_output


def print_tree(root_node: Node) -> None:
    for pre, fill, node in RenderTree(root_node):
        print("%s%s" % (pre, node.name))


def node_is_file_or_empty_directory(node: Node) -> bool:
    return node.is_leaf


def compute_node_size_and_register_directory_sizes(node: Node, directory_to_size_map: dict) -> int:
    if node_is_file_or_empty_directory(node):
        return node.size
    else:
        directory_size = sum(
            [compute_node_size_and_register_directory_sizes(child, directory_to_size_map) for child in node.children])
        directory_to_size_map[str(node.path)] = directory_size
        return directory_size


def parse_terminal_output(terminal_output: list[str]) -> Node:
    root_directory = Node('/')

    current_directory = root_directory
    for line in terminal_output:
        if line == '$ cd ..':
            current_directory = current_directory.parent
        elif line.startswith('$ cd'):
            directory_name = line.split()[2]
            current_directory = Node(name=directory_name, parent=current_directory, size=0)
        elif not line.startswith('dir'):
            filename, filesize = line.split()[1], int(line.split()[0])
            file_node = Node(name=filename, parent=current_directory, size=filesize)
    return root_directory


def first_part(directory_to_size_map: dict) -> int:
    directory_sizes_at_most_100000: list[int] = \
        [size for size in directory_to_size_map.values() if size <= 100000]
    return sum(directory_sizes_at_most_100000)


def second_part(directory_to_size_map: dict) -> int:
    required_unused_space = 30000000
    total_disk_space = 70000000
    sizes = directory_to_size_map.values()
    root_directory_size = max(sizes)
    current_unused_space = total_disk_space - root_directory_size
    sizes_of_directories_that_can_leave_enough_space = filter(
        lambda size: current_unused_space + size >= required_unused_space, sizes)
    size_of_directory_to_delete = min(sizes_of_directories_that_can_leave_enough_space)
    return size_of_directory_to_delete


def main():
    terminal_output_input = read_input('input.txt')
    root_directory: Node = parse_terminal_output(terminal_output_input)
    directory_to_size_map = dict()
    compute_node_size_and_register_directory_sizes(root_directory, directory_to_size_map)
    print(f'Result for the first part : {first_part(directory_to_size_map)}')
    print(f'Result for the second part : {second_part(directory_to_size_map)}')


if __name__ == '__main__':
    main()
