def read_input(input_path: str) -> list[str]:
    with open(input_path, 'r') as input_file:
        calories_list = [line.rstrip() for line in input_file.readlines()]
        calories_list.append('')
    return calories_list


def first_part(calories_per_elf: list[int]) -> int:
    return max(calories_per_elf)


def second_part(calories_per_elf: list[int]) -> int:
    sorted_calories_per_elf = sorted(calories_per_elf, reverse=True)
    sum_top_3_calories = sum(sorted_calories_per_elf[:3])
    return sum_top_3_calories


def main():
    calories_input_list = read_input('input.txt')
    calories_per_elf_list = []
    current_elf = 0
    for calory in calories_input_list:
        if calory != '':
            current_elf += int(calory)
        else:
            calories_per_elf_list.append(current_elf)
            current_elf = 0
    print(f'Result for the first part : {first_part(calories_per_elf_list)}')
    print(f'Result for the second part : {second_part(calories_per_elf_list)}')


if __name__ == '__main__':
    main()
