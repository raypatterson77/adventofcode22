def main():
    with open('input.txt') as challenge_input:
        full_overlaps = 0
        overlaps = 0
        for line in challenge_input:
            stripped_line = line.strip()
            first_elve, second_elve = stripped_line.split(",")
            first_elve = [int(x) for x in (first_elve.split("-"))]
            second_elve = [int(x) for x in (second_elve.split("-"))]
            if first_elve[0] >= second_elve[0] and first_elve[1] <= second_elve[1] or \
                first_elve[0] <= second_elve[0] and first_elve[1] >= second_elve[1]:
                full_overlaps += 1
            # part 2
            if first_elve[0] in range(second_elve[0], second_elve[1]+1) or first_elve[1] in range(second_elve[0], second_elve[1]+1) \
                or second_elve[0] in range(first_elve[0], first_elve[1]+1) or second_elve[1] in range(first_elve[0], first_elve[1]+1):
                overlaps += 1
    print("full overlaps: %d" % full_overlaps)
    print("overlaps: %d" % overlaps)

if __name__ == '__main__':
    main()
