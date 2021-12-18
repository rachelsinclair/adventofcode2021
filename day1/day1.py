import unittest

def get_count_of_times_that_value_increases(sequence: list):
    value_pairs = zip(sequence, sequence[1:])
    count = 0
    for previous_value, current_value in value_pairs:
        if current_value > previous_value:
            count = count + 1
    return count

def get_all_three_value_windows(sequence: list):
    return list(zip(sequence, sequence[1:], sequence[2:]))

def get_list_of_sums_of_tuples(input_list: list):
    return [sum(item) for item in input_list]

def get_puzzle_input():
    with open('input.txt') as input_file:
        return [int(line) for line in input_file.read().splitlines()]

def solve_part_1():
    puzzle_input = get_puzzle_input()
    return get_count_of_times_that_value_increases(puzzle_input)

def solve_part_2():
    puzzle_input = get_puzzle_input()
    measurement_windows = get_all_three_value_windows(puzzle_input)
    measurement_window_sums = get_list_of_sums_of_tuples(measurement_windows)
    count_of_increases_in_sums = get_count_of_times_that_value_increases(measurement_window_sums)
    return count_of_increases_in_sums

part_1_solution = solve_part_1()
print(f"Solution to part 1: {part_1_solution}")

part_2_solution = solve_part_2()
print(f"Solution to part 1: {part_2_solution}")

class TestGetCountOfTimesThatValueIncreases(unittest.TestCase):

    def test_empty_list_returns_0(self):
        self.assertEqual(get_count_of_times_that_value_increases([]), 0)
    
    def test_list_with_single_item_returns_0(self):
        self.assertEqual(get_count_of_times_that_value_increases([1]), 0)

    def test_single_increasing_pair_returns_1(self):
        self.assertEqual(get_count_of_times_that_value_increases([1,2]), 1)

    def test_single_decreasing_pair_returns_0(self):
        self.assertEqual(get_count_of_times_that_value_increases([2,1]), 0)
class TestGetAllThreeValueWindows(unittest.TestCase):

    def test_list_with_length_below_3_returns_empty_list(self):
        self.assertEqual(get_all_three_value_windows([]), [])
        self.assertEqual(get_all_three_value_windows([1]), [])
        self.assertEqual(get_all_three_value_windows([1,2]), [])
    
    def test_list_with_length_3_returns_a_single_tuple(self):
        self.assertEqual(get_all_three_value_windows([1,2,3]), [(1,2,3)])

    def test_list_with_length_4_returns_two_tuples(self):
        self.assertEqual(get_all_three_value_windows([1,2,3,4]), [(1,2,3), (2,3,4)])
class TestGetListOfSumsOfTuples(unittest.TestCase):

    def test_empty_list_returns_empty_list(self):
        self.assertEqual(get_list_of_sums_of_tuples([]), [])
    
    def test_list_with_length_3_returns_a_single_tuple(self):
        self.assertEqual(get_list_of_sums_of_tuples([(1,2,3)]), [6])

    def test_list_with_length_4_returns_two_tuples(self):
        self.assertEqual(get_list_of_sums_of_tuples([(1,2,3), (2,3,4)]), [6, 9])

if __name__ == "__main__":
    unittest.main()