import math


class ForestGrid():
    height: int
    width: int
    content: list[list[int]]
    directions: list[str]

    def __init__(self, content: list[list[int]]):
        self._content = content
        self.height = len(content)
        self.width = len(content[0])
        self.directions = ['top', 'bottom', 'left', 'right']


    def get_tree_height(self, i: int, j: int) -> int:
        return self._content[i][j]


    def is_tree_on_edge(self, i: int, j: int) -> bool:
        return (i == 0) or (i == self.height - 1) or (j == 0) or (j == self.width - 1)


    def is_tree_visible_from(self, direction: str, i: int, j: int) -> bool:
        tree_height = self.get_tree_height(i, j)
        if direction == 'top':
            return all(self.get_tree_height(i_iter, j) < tree_height for i_iter in range(i))
        elif direction == 'left':
            return all(self.get_tree_height(i, j_iter) < tree_height for j_iter in range(j))
        elif direction == 'right':
            return all(self.get_tree_height(i, j_iter) < tree_height for j_iter in range(self.width - 1, j, -1))
        elif direction == 'bottom':
            return all(self.get_tree_height(i_iter, j) < tree_height for i_iter in range(self.height - 1, i, -1))


    def is_tree_visible(self, i, j):
        return self.is_tree_on_edge(i, j) or any(
            self.is_tree_visible_from(direction, i, j) for direction in self.directions)


    def count_visible_trees(self) -> int:
        nb_visible_trees = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.is_tree_visible(i, j):
                    nb_visible_trees += 1
        return nb_visible_trees


    def compute_viewing_distance_from(self, direction: str, i: int, j: int) -> int:
        nb_smaller_trees_in_a_row = 0
        tree_height = self.get_tree_height(i, j)
        range_for_loop = None

        if direction == 'top':
            range_for_loop = range(i - 1, -1, -1)
        elif direction == 'bottom':
            range_for_loop = range(i + 1, self.height)
        elif direction == 'left':
            range_for_loop = range(j - 1, -1, -1)
        elif direction == 'right':
            range_for_loop = range(j + 1, self.width)

        if direction == 'top' or direction == 'bottom':
            for i_iter in range_for_loop:
                nb_smaller_trees_in_a_row += 1
                if tree_height <= self.get_tree_height(i_iter, j):
                    break
        else:
            for j_iter in range_for_loop:
                nb_smaller_trees_in_a_row += 1
                if tree_height <= self.get_tree_height(i, j_iter):
                    break
        return nb_smaller_trees_in_a_row


    def compute_scenic_score(self, i: int, j: int) -> int:
        viewing_distances = [self.compute_viewing_distance_from(direction, i, j) for direction in
                             self.directions]
        return math.prod(viewing_distances)


    def get_max_scenic_score(self):
        scenic_scores: list[int] = []
        for i in range(self.height):
            for j in range(self.width):
                scenic_scores.append(self.compute_scenic_score(i, j))
        return max(scenic_scores)
