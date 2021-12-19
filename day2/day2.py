import unittest
from math import prod

def calculate_single_displacement(direction: str, magnitude: int):
    if direction == "forward":
        return (magnitude,0)
    elif direction == "down":
        return (0, magnitude)
    elif direction == "up":
        return (0, -magnitude)
    else:
        raise ValueError('Direction not recognised') 

def calculate_displacement_list_from_instructions(instruction_list: list):
    return [calculate_single_displacement(*instruction) for instruction in instruction_list]

def sum_of_displacements(displacements: list):
    if len(displacements) == 0:
        return (0,0)
    total_displacement = tuple(sum(axis) for axis in zip(*displacements))
    return total_displacement

def get_puzzle_input():
    with open('input.txt') as input_file:
        lines = input_file.read().splitlines()
        return [tuple([line.split(' ')[0], int(line.split(' ')[1])]) for line in lines]

def solve_part_1():
    origin = (0,0)
    puzzle_input = get_puzzle_input()
    displacement_list = calculate_displacement_list_from_instructions(puzzle_input)
    total_displacement = sum_of_displacements(displacement_list)
    return prod(total_displacement)

def solve_part_2():
    puzzle_input = get_puzzle_input()
    return 0

part_1_solution = solve_part_1()
print(f"Solution to part 1: {part_1_solution}")

part_2_solution = solve_part_2()
print(f"Solution to part 1: {part_2_solution}")

class TestCalculateSingleDisplacement(unittest.TestCase):

    def test_forward_command_adds_horizontal_displacement(self):
        self.assertEqual(calculate_single_displacement("forward", 1),(1,0))

    def test_down_command_increases_vertical_displacement(self):
        self.assertEqual(calculate_single_displacement("down", 1),(0,1))

    def test_up_command_decreases_vertical_displacement(self):
        self.assertEqual(calculate_single_displacement("up", 1),(0,-1))

    def test_unhandled_direction_throws_valueerror(self):
        with self.assertRaises(ValueError) as error:
            calculate_single_displacement("backwards", 1)
        self.assertEqual("Direction not recognised", str(error.exception))

class TestCalculateDisplacementList(unittest.TestCase):
    def test_creates_list_of_displacements_from_list_of_instructions(self):
        instruction_list = [("forward", 5),("down", 5),("forward", 8),("up", 3),("down", 8),("forward", 2)]
        expected_result = [(5,0),(0,5),(8,0),(0,-3),(0,8),(2,0)]
        self.assertEqual(calculate_displacement_list_from_instructions(instruction_list), expected_result)

class TestSumOfDisplacements(unittest.TestCase):
    def test_empty_list_returns_zeroes(self):
        self.assertEqual(sum_of_displacements([]), (0,0))

    def test_single_tuple_returns_itself(self):
        self.assertEqual(sum_of_displacements([(0,1)]), (0,1))

    def test_two_tuples_returns_correct_sum(self):
        self.assertEqual(sum_of_displacements([(1,0),(0,2)]), (1,2))


if __name__ == "__main__":
    unittest.main()