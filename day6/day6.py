from collections import Counter

def get_unique_slice_index(challenge_slices):
    for string_slice in challenge_slices:
        number_of_chars = Counter(string_slice)
        counter +=1
        if(len(number_of_chars) == len(string_slice)):
            return challenge_slices.index(string_slice)

def main():
    solution_part1 = ""
    solution_part2 = ""
    size_part1 = 4
    size_part2 = 14
    with open('input.txt') as challenge_input:
        challenge_input_lines = challenge_input.read()
        challenge_input_lines = challenge_input_lines.strip()        
        string_slices = [challenge_input_lines[char_pos:char_pos+size_part1] for char_pos in range(0, len(challenge_input_lines)-size_part1 + 1)]
        message_slices = [challenge_input_lines[char_pos:char_pos+size_part2] for char_pos in range(0, len(challenge_input_lines)-size_part2 + 1)]
        uniquie_slice_index = get_unique_slice_index(string_slices)
        unique_message_index = get_unique_slice_index(message_slices)
        solution_part1 = (uniquie_slice_index)+4
        solution_part2 = (unique_message_index)+14
        print("solution part 1 is %d" % solution_part1)
        print("solution part 2 is %d" % solution_part2)

if __name__ == '__main__':
    main()
