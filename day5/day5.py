def build_stacks(crates_list):
    all_stacks = []
    stack_1 = []
    stack_2 = []
    stack_3 = []
    stack_4 = []
    stack_5 = []
    stack_6 = []
    stack_7 = []
    stack_8 = []
    stack_9 = []

    stack_positions = slice(1,323,4)
    stack_elements = crates_list[stack_positions]
    
    for i in range(0,81,9):
        stack_1.append(stack_elements[i])
        stack_2.append(stack_elements[i+1])
        stack_3.append(stack_elements[i+2])
        stack_4.append(stack_elements[i+3])
        stack_5.append(stack_elements[i+4])
        stack_6.append(stack_elements[i+5])
        stack_7.append(stack_elements[i+6])
        stack_8.append(stack_elements[i+7])
        stack_9.append(stack_elements[i+8])
    
    stack_1.reverse()
    stack_2.reverse()
    stack_3.reverse()
    stack_4.reverse()
    stack_5.reverse()
    stack_6.reverse()
    stack_7.reverse()
    stack_8.reverse()
    stack_9.reverse()

    stack_1 = " ".join(stack_1).split()
    stack_2 = " ".join(stack_2).split()
    stack_3 = " ".join(stack_3).split()
    stack_4 = " ".join(stack_4).split()
    stack_5 = " ".join(stack_5).split()
    stack_6 = " ".join(stack_6).split()
    stack_7 = " ".join(stack_7).split()
    stack_8 = " ".join(stack_8).split()
    stack_9 = " ".join(stack_9).split()

    all_stacks.append(stack_1)
    all_stacks.append(stack_2)
    all_stacks.append(stack_3)
    all_stacks.append(stack_4)
    all_stacks.append(stack_5)
    all_stacks.append(stack_6)
    all_stacks.append(stack_7)
    all_stacks.append(stack_8)
    all_stacks.append(stack_9)
    
    return all_stacks

def build_instructions(instructions):
    instruction_list = []
    for instruction in instructions.split("\n"):
        one_instruction = []
        for element in instruction.split(" "):
            if element.strip().isnumeric():
                one_instruction.append(int(element))
        if len(one_instruction) == 3:
            instruction_list.append(one_instruction)
    return instruction_list

def make_movements_part1(instruction_list, all_stacks_part1):
    for instruction in instruction_list:
        for i in range(0,instruction[0]):
            all_stacks_part1[instruction[2]-1].append(all_stacks_part1[instruction[1]-1].pop())
    return all_stacks_part1

def make_movements_part2(instruction_list, all_stacks_part2):
    temp_stack = []
    for instruction in instruction_list:
        for i in range(0,instruction[0]):
            temp_stack.append(all_stacks_part2[instruction[1]-1].pop())
        temp_stack.reverse()
        all_stacks_part2[instruction[2]-1] = all_stacks_part2[instruction[2]-1] + temp_stack
        temp_stack = []
    return all_stacks_part2

def main():
    solution_part1 = ""
    solution_part2 = ""
    with open('input.txt') as challenge_input:
        challenge_input_lines = challenge_input.read()
        start_crates = challenge_input_lines.split("\n\n")[0].strip()
        instructions = challenge_input_lines[325:]
        all_stacks_part1 = build_stacks(start_crates)
        all_stacks_part2 = build_stacks(start_crates)
        instruction_list = build_instructions(instructions)
        final_stacks_part1 = make_movements_part1(instruction_list, all_stacks_part1)
        final_stacks_part2 = make_movements_part2(instruction_list, all_stacks_part2)
        for stack in final_stacks_part1:
            solution_part1 = solution_part1 + stack[-1]
        for stack in final_stacks_part2:
            solution_part2 = solution_part2 + stack[-1]
        print("final order part1 is %s" % solution_part1)
        print("final order part2 is %s" % solution_part2)

if __name__ == '__main__':
    main()