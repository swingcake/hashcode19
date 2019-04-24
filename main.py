import os
from file_reader import read_file
from file_writer import write_output
from problem_solver import ProblemSolver

# Input

files = ['a_example.txt', 'b_lovely_landscapes.txt', 'c_memorable_moments.txt', 'd_pet_pictures.txt', 'e_shiny_selfies.txt']

# End Input

example_file = os.path.join('data', files[0])
example = read_file(example_file)
exampleSlicer = ProblemSolver(example['header'], example['rows'], os.path.join('output', 'example.txt'))
exampleSlicer.output_solution()

small_file = os.path.join('data', files[1])
small = read_file(small_file)
smallSlicer = ProblemSolver(small['header'], small['rows'], os.path.join('output', 'small.txt'))
smallSlicer.output_solution()

medium_file = os.path.join('data', files[2])
medium = read_file(medium_file)
mediumSlicer = ProblemSolver(medium['header'], medium['rows'], os.path.join('output', 'medium.txt'))
mediumSlicer.output_solution()

big_file = os.path.join('data', files[3])
big = read_file(big_file)
bigSlicer = ProblemSolver(big['header'], big['rows'], os.path.join('output', 'big.txt'))
bigSlicer.output_solution()

biggest_file = os.path.join('data', files[4])
biggest = read_file(biggest_file)
biggestSlicer = ProblemSolver(biggest['header'], biggest['rows'], os.path.join('output', 'biggest.txt'))
biggestSlicer.output_solution()


