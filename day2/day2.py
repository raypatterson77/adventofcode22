#my_* for part1
my_points = {"X":1, "Y":2, "Z":3}
#must_* fort part2
must_points = points = {"X":0, "Y":3, "Z":6}
opponent_points = {"A":1, "B":2, "C":3}
my_lose = {3:1, 1:2, 2:3}
my_win = {2:1, 3:2, 1:3}
must_lose = {1:3, 2:1, 3:2}
must_win = {1:2, 2:3, 3:1}

def main():
    my_score = 0
    must_score = 0 
    with open('input.txt') as challenge_input:
        for line in challenge_input:
            my_choice = line.split(" ")[1].strip()
            opponents_choice = line.split(" ")[0].strip()
            opponents_choice_int = opponent_points[opponents_choice]
            my_choice_int = my_points[my_choice]
            if my_win[my_choice_int] == opponents_choice_int:
                my_score = my_score + my_choice_int + 6
            elif my_lose[my_choice_int] == opponents_choice_int:
                my_score = my_score + my_choice_int + 0   
            else:
                my_score = my_score + my_choice_int + 3
            
            #part 2:
            if must_points[my_choice] == 0:
                must_score = must_score + must_lose[opponents_choice_int] + must_points[my_choice]
            elif must_points[my_choice] == 6:
                must_score = must_score + must_win[opponents_choice_int] + must_points[my_choice]
            else:
                must_score = must_score + opponents_choice_int + must_points[my_choice]
    print("my score part1 is %d" % my_score)
    print("my score part2 is %d" % must_score)

if __name__ == '__main__':
    main()
