#!/usr/bin/env python

class Regs(dict):
    def __getitem__(self, item):
        # Set it to zero first
        if item not in super().keys():
            self[item] = 0

        return super().__getitem__(item)

def condition_is_true(condition):
    global regs
    reg = condition.split(" ")[0]
    condition = condition.replace(reg, "regs['{}']".format(reg))
    return eval(condition)

def eval_instruction(instruction):
    global regs
    reg, command, val = instruction.split(" ")
    val = int(val, 10)

    if command == "inc":
        regs[reg] += val
    elif command == "dec":
        regs[reg] -= val
    else:
        print("unknown command: " + command)


with open("input","r") as f:
    inp = f.read().strip()

regs = Regs()
highest = 0

for line in inp.split("\n"):
    line = line.strip()

    condition = line.split(" if ")[1]

    if condition_is_true(condition):
        eval_instruction(line.split(" if ")[0])

    current_highest = regs[sorted(regs, key=lambda x: regs[x])[-1]]
    highest = current_highest if current_highest > highest else highest

# Part 1
print(regs[sorted(regs, key=lambda x: regs[x])[-1]])

# Part 2
print(highest)
