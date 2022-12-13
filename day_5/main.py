import copy
import re
from typing import Callable


def split_into_stack_item(input_instruction_string: str) -> list[str]:
    first_item_index = 1
    step_between_each_item = 4
    return [input_instruction_string[i] for i in
            range(first_item_index, len(input_instruction_string), step_between_each_item)]


def remove_whitespaces_top_of_stacks(stack_items_list: list[list[str]]) -> list[list[str]]:
    for stack in stack_items_list:
        reversed_stack = stack[::-1]
        item_index = 0
        while item_index in range(len(stack)) and reversed_stack[item_index] == ' ':
            stack.pop()
            item_index += 1
    return stack_items_list


def parse_stack_information(stack_string: str) -> list[list[str]]:
    nb_stacks = int(stack_string[-1])
    items_for_each_line_list = stack_string.split('\n')[::-1][1:]
    biggest_stack_length = len(items_for_each_line_list)
    stack_items_list = [[] for _ in range(nb_stacks)]
    for line in range(biggest_stack_length):
        items_per_stack_in_line = split_into_stack_item(items_for_each_line_list[line])
        nb_items = len(items_per_stack_in_line)
        for stack_index in range(nb_items):
            stack_items_list[stack_index].append(items_per_stack_in_line[stack_index])
    stack_items_list = remove_whitespaces_top_of_stacks(stack_items_list)
    return stack_items_list


def parse_instruction_list(instruction_string: str) -> list[list[int]]:
    instruction_list = instruction_string.split('\n')
    instruction_list = [re.sub(r'[A-Za-z]+', '', instruction).split() for instruction in instruction_list]
    instruction_list = [list(map(int, instruction)) for instruction in instruction_list]
    return instruction_list


def read_input(input_path: str) -> tuple[list[list[str]], list[list[int]]]:
    with open(input_path, 'r') as input_file:
        input = input_file.read()
        input = input.split('\n\n')
        stack_items_list = parse_stack_information(input[0])
        instruction_list = parse_instruction_list(input[1])
    return stack_items_list, instruction_list


def move_crate_one_at_a_time(origin_stack: list[str], dest_stack: list[str], nb_items_to_move) -> None:
    for _ in range(nb_items_to_move):
        item_to_move = origin_stack.pop()
        dest_stack.append(item_to_move)


def move_crate_multiple_ones_at_a_time(origin_stack: list[str], dest_stack: list[str], nb_items_to_move) -> None:
    items_to_move = origin_stack[-nb_items_to_move:]
    dest_stack.extend(items_to_move)
    for _ in range(nb_items_to_move):
        origin_stack.pop()


def apply_instruction_list_to_stack_list(input_tuple: tuple[list[list[str]], list[list[int]]],
                                         move_crates_function: Callable) -> str:
    stack_items_list, instruction_list = copy.deepcopy(input_tuple[0]), input_tuple[1]
    for instruction in instruction_list:
        origin_stack = stack_items_list[instruction[1] - 1]
        dest_stack = stack_items_list[instruction[2] - 1]
        nb_items_to_move = instruction[0]
        move_crates_function(origin_stack, dest_stack, nb_items_to_move)
    output_stack_top_crates = ''.join([stack[-1] for stack in stack_items_list])
    return output_stack_top_crates


def first_part(input_tuple: tuple[list[list[str]], list[list[int]]]) -> str:
    return apply_instruction_list_to_stack_list(input_tuple, move_crate_one_at_a_time)


def second_part(input_tuple: tuple[list[list[str]], list[list[int]]]) -> str:
    return apply_instruction_list_to_stack_list(input_tuple, move_crate_multiple_ones_at_a_time)


def main():
    input = read_input('input.txt')
    print(f'Result for the first part : {first_part(input)}')
    print(f'Result for the second part : {second_part(input)}')


if __name__ == '__main__':
    main()
