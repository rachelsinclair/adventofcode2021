import unittest

def get_puzzle_input():
    with open('input.txt') as input_file:
        return input_file.read().splitlines()

def solve_part_1():
    puzzle_input = get_puzzle_input()
    print (puzzle_input[:5])
    return 0

def solve_part_2():
    puzzle_input = get_puzzle_input()
    return 0

part_1_solution = solve_part_1()
print(f"Solution to part 1: {part_1_solution}")

part_2_solution = solve_part_2()
print(f"Solution to part 1: {part_2_solution}")

class TestDummy(unittest.TestCase):

    def test_dummy_test(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()