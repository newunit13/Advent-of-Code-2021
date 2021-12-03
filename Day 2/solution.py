
# set up data
with open('Day 2/input.txt', 'r') as f:
    raw_data = f.readlines()
    commands = []
    for line in raw_data:
        command, value = line.split()
        value = int(value)
        commands.append((command, value))


# Part 1
    command_log = {}
    for command, value in commands:
        if command not in command_log:
            command_log[command] = [value]
        else:
            command_log[command].append(value)

answer = sum(command_log['forward']) * (sum(command_log['down']) - sum(command_log['up']))
print(answer) # 1654760


# Part 2

from dataclasses import dataclass

@dataclass
class Ship:
    _forward: int
    _aim: int
    _depth: int

    def process_command(self, command, amount):

        if command == 'forward':
            self._forward += amount
            if self._aim != 0:
                self._depth += self._aim * amount
        elif command == 'up':
            self._aim -= amount
        elif command == 'down':
            self._aim += amount
        else:
            raise ValueError('Invalid direction')

my_ship = Ship(0, 0, 0)

for command, value in commands:
    my_ship.process_command(command, value)

answer = my_ship._forward * my_ship._depth

print(answer) # 1956047400