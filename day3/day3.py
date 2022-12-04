def translate_to_ints(string_line):
    int_line = []
    for line in string_line:
        if ord(line) < 97:
            int_line.append(ord(line)-38)
        else:
            int_line.append(ord(line)-96)
    return int_line

def find_same_items(first_half, second_half):
    points_counter = 0
    same_items = set(first_half).intersection(set(second_half))
    for item in same_items:
        points_counter += item
    return points_counter

def find_badge(elve_group):
    badge = set(elve_group[0]).intersection(set(elve_group[1]), set(elve_group[2]))
    badge_points = list(badge)[0]
    return badge_points

def main():
    sum_of_same_items = 0
    #part2
    elve_group_list = []
    sum_of_badges = 0
    badge_points  = 0
    with open('input.txt') as challenge_input:
        for line in challenge_input:
            stripped_line = line.strip()
            int_line = translate_to_ints(stripped_line)
            #part_two
            elve_group_list.append(int_line) 
            if len(elve_group_list) == 3:
                badge_points = find_badge(elve_group_list)
                sum_of_badges += badge_points
                elve_group_list = []
            middle_index = int(len(int_line)/2)
            first_half = int_line[:middle_index]
            second_half = int_line[middle_index:]
            sum_of_same_items = sum_of_same_items + find_same_items(first_half, second_half)
    print("Sum of same item priorites %d" % sum_of_same_items)
    print("Sum of same badge priorites %d" % sum_of_badges)

if __name__ == '__main__':
    main()