def read_input(input_path: str) -> str:
    with open(input_path, 'r') as input_file:
        datastream_buffer = input_file.read()
    return datastream_buffer


def toto(datastream_buffer_input: str, offset: int) -> int:
    for i in range(len(datastream_buffer_input)):
        packet_start = datastream_buffer_input[i:i + offset]
        characters_all_distinct = len(set(packet_start)) == offset
        if characters_all_distinct :
            return i + offset


def first_part(datastream_buffer_input: str) -> int:
    return toto(datastream_buffer_input, offset=4)


def second_part(datastream_buffer_input: str):
    return toto(datastream_buffer_input, offset=14)


def main():
    datastream_buffer_input = read_input('input.txt')
    print(f'Result for the first part : {first_part(datastream_buffer_input)}')
    print(f'Result for the second part : {second_part(datastream_buffer_input)}')


if __name__ == '__main__':
    main()
