import typing


def read_input(input_path: str) -> list[list[str]]:
    with open(input_path, 'r') as input_file:
        assignment_pairs = [line.rstrip().split(',') for line in input_file.readlines()]
    return assignment_pairs


def get_assignment_range(assignment: str) -> range:
    start_end_section_list = [int(section_id) for section_id in assignment.split('-')]
    return range(start_end_section_list[0], start_end_section_list[1] + 1)


def check_full_overlapping(first_assignment: range, second_assignment: range) -> bool:
    assert len(first_assignment) != 0 and len(second_assignment) != 0, 'One range is empty, overlaps count will be false'
    return all(section_id in first_assignment for section_id in second_assignment) or all(
        section_id in second_assignment for section_id in first_assignment)

def check_partial_overlapping(first_assignment: range, second_assignment: range) -> bool:
    assert len(first_assignment) != 0 and len(second_assignment) != 0, 'One range is empty, overlaps count will be false'
    return any(section_id in first_assignment for section_id in second_assignment) or any(
        section_id in second_assignment for section_id in first_assignment)


def solution(assignment_pairs_input_list: list[list[str]], overlapping_function : typing.Callable) -> int:
    nb_overlaps = 0
    for assignment_pair in assignment_pairs_input_list:
        first_elf_assignment_range = get_assignment_range(assignment_pair[0])
        second_elf_assignment_range = get_assignment_range(assignment_pair[1])
        if overlapping_function(first_elf_assignment_range, second_elf_assignment_range):
            nb_overlaps += 1
    return nb_overlaps

def main():
    assignment_pairs_input_list = read_input('input.txt')
    print(f'Result for the first part : {solution(assignment_pairs_input_list, check_full_overlapping)}')
    print(f'Result for the second part : {solution(assignment_pairs_input_list, check_partial_overlapping)}')

if __name__ == '__main__':
    main()
