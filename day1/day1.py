def main():
    with open('input.txt') as challenge_input:
        all_calories = []
        elve_calories = 0
        sum_three_highest_calories = 0
        for line in challenge_input:
            if line.strip() != "":
                elve_calories += int(line.strip())
            else:
                all_calories.append(elve_calories)
                elve_calories = 0
        #add calories after last loop
        all_calories.append(elve_calories)
        all_calories_sorted = sorted(all_calories, reverse=True)
        for i in range(0,3):
            sum_three_highest_calories = sum_three_highest_calories + all_calories_sorted[i]
        print("highest calories %d" % all_calories_sorted[0])
        print("thee highest calories combined %d" % sum_three_highest_calories)
        
if __name__ == '__main__':
    main()