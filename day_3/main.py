import string


def get_item_priority(item: str) -> int:
    assert len(item) == 1, 'Wrong item, must be a single letter'
    items_priority_order_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return items_priority_order_string.index(item) + 1


def read_input(input_path: str) -> list[str]:
    with open(input_path, 'r') as input_file:
        rucksacks = [line.rstrip() for line in input_file.readlines()]
    return rucksacks


def first_part(rucksacks_input_list: list[str]) -> int:
    priority_sum = 0
    for rucksack in rucksacks_input_list:
        first_half = rucksack[:len(rucksack) // 2]
        second_half = rucksack[len(rucksack) // 2:]
        common_item_set = set(first_half) & set(second_half)
        common_item = max(common_item_set)
        priority_sum += get_item_priority(common_item)
    return priority_sum


def second_part(rucksacks_input_list: list[str]):
    priority_sum = 0
    group_size = 3
    rucksacks_divided_by_groups = zip(*(iter(rucksacks_input_list),) * group_size)

    for group_rucksacks in rucksacks_divided_by_groups:
        group_badge_as_set = set(group_rucksacks[0]).intersection(set(group_rucksacks[1]), set(group_rucksacks[2]))
        group_badge_item = max(group_badge_as_set)
        priority_sum += get_item_priority(group_badge_item)
    return priority_sum


def main():
    rucksacks_input_list = read_input('input.txt')
    print(f'Result for the first part : {first_part(rucksacks_input_list)}')
    print(f'Result for the second part : {second_part(rucksacks_input_list)}')


if __name__ == '__main__':
    main()
