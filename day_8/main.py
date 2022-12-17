from day_8.ForestGrid import ForestGrid


def read_input(input_path: str) -> list[list[int]]:
    with open(input_path, 'r') as input_file:
        grid = [[int(tree_height) for tree_height in line.strip()] for line in input_file.readlines()]
    return grid


def first_part(grid: ForestGrid) -> int:
    return grid.count_visible_trees()


def second_part(grid: ForestGrid) -> int:
    return grid.get_max_scenic_score()


def main():
    tree_grid_input: list[list[int]] = read_input('input.txt')
    tree_grid = ForestGrid(tree_grid_input)
    print(f'Result for the first part : {first_part(tree_grid)}')
    print(f'Result for the second part : {second_part(tree_grid)}')


if __name__ == '__main__':
    main()
