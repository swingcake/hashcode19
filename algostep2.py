import os
from file_reader import read_file
from file_writer import write_output
from problem_solver import ProblemSolver
from Slide import Slide
# Input

files = ['a_example.txt', 'b_loveley_landscapes.txt', 'c_memorable_moments.txt', 'd_pet_pictures.txt', 'e_shiny_selfies.txt']

# End Input

example_file = os.path.join('data', files[0])
example = read_file(example_file)

print(example)
' will change to slide from their function'
photos = example['rows']
slides = [] # they will pass this
for photo in photos:
    if photo['orientation'] == 'H':
        # print(photo['tags'])
        slides.append(Slide(photo))
''''''


