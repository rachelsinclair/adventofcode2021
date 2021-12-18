import unittest

def get_count_of_times_that_depth_increases(sequence: list):
    depth_pairs = zip(sequence, sequence[1:])
    count = 0
    for previous_depth, current_depth in depth_pairs:
        if current_depth > previous_depth:
            count = count + 1
    return count

def get_puzzle_input():
    with open('input.txt') as input_file:
        return [int(line) for line in input_file.read().splitlines()]

def solve_part_1():
    puzzle_input = get_puzzle_input()
    return get_count_of_times_that_depth_increases(puzzle_input)

part_1_solution = solve_part_1()
print(f"Solution to part 1: {part_1_solution}")

class TestGetCountOfTimesThatDepthIncreases(unittest.TestCase):

    def test_empty_list_returns_0(self):
        self.assertEqual(get_count_of_times_that_depth_increases([]), 0)
    
    def test_list_with_single_item_returns_0(self):
        self.assertEqual(get_count_of_times_that_depth_increases([1]), 0)

    def test_single_increasing_pair_returns_1(self):
        self.assertEqual(get_count_of_times_that_depth_increases([1,2]), 1)

    def test_single_decreasing_pair_returns_0(self):
        self.assertEqual(get_count_of_times_that_depth_increases([2,1]), 0)

if __name__ == "__main__":
    unittest.main()