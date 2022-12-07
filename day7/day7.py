from collections import defaultdict
from itertools import accumulate

def main():
    folder_sizes= defaultdict(int)
    folders_visited = []
    solution_part1 = 0
    solution_part2 = 0 
    temp_list_solution_part2 = []
    with open("input.txt") as challenge_input:
        for line in challenge_input:
            line_parts = line.strip().split(" ")
            match line_parts:
                case "$", "cd", "/": 
                    folders_visited.append(line_parts[2])
                case "$", "cd", "..":
                    folders_visited.pop()
                case "$", "cd", folder:
                    folders_visited.append(line_parts[2])
                case other_commands:
                    if line_parts[0].isnumeric():
                        for folder in accumulate(folders_visited):
                            folder_sizes[folder] += int(line_parts[0])
    #part1              
    for _,folder in folder_sizes.items():
        if folder <= 100000:
            solution_part1 += folder
    #part2
    minimun_space = folder_sizes["/"]-40000000
    for _,folder in folder_sizes.items():
        if folder >= minimun_space:
            temp_list_solution_part2.append(folder)
    solution_part2 = min(temp_list_solution_part2)
    print("solution part1 is %d" % solution_part1)
    print("solution part2 is %d" % solution_part2)

if __name__ == "__main__":
    main()