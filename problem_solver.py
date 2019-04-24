from SlideShow import SlideShow
from Picture import Picture
from file_writer import write_output

class ProblemSolver:

    def __init__(self, header, rows, output_file):
        self.output_file = output_file
        self.num_photos = header
        self.pictures = []
        for row in rows:
            self.pictures.append(Picture(row))
        self.slideShow = SlideShow(self.pictures)


    def output_solution(self):
        print("Score: {}".format(self.slideShow.get_score()))
        output = []
        output.append(self.slideShow.get_num_slides())
        output += self.slideShow.get_slide_ids()
        write_output(self.output_file, output)