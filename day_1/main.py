
if __name__ == '__main__':
    input_path = 'input.txt'
    with open(input_path, 'r') as input_file :
        calories = [line.rstrip() for line in input_file.readlines()]
        print(calories)

    calories.append('')
    calories_per_elf = []
    current_elf = 0
    for calory in calories :
        if calory != '' :
            current_elf += int(calory)
        else :
            calories_per_elf.append(current_elf)
            current_elf = 0

    sorted_calories_per_elf = sorted(calories_per_elf, reverse=True)
    sum_top_3_calories = sum(sorted_calories_per_elf[:3])
    print(max(sorted_calories_per_elf))
    print(sorted_calories_per_elf)
    print(sum_top_3_calories)


