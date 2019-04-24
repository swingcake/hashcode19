import copy
from Slide import Slide

class SlideShow:
    def __init__(self, pictures):
        self.pictures = pictures
        self.slides = self.create_slides()

    def create_slides(self):
        pictures_copy = copy.deepcopy(self.pictures)
        slides = []

        my_sorted_verticles = self.sortVerticalsByDifficulty()
        print(my_sorted_verticles)

        while len(pictures_copy) != 0:
            picture = pictures_copy[0]
            if picture.orientation == "H":
                slides.append(Slide(picture))
            else:
                best_match_index = self.get_best_vertical_match(picture, pictures_copy)
                if best_match_index is not None:
                    slides.append(Slide(picture, pictures_copy[best_match_index]))
                    del pictures_copy[best_match_index]
            del pictures_copy[0]
        return slides

    def createVerticalList(self):
        pictures_copy = copy.deepcopy(self.pictures)
        verticle_slides = []
        for picture in pictures_copy:
            if picture.orientation == 'V':
                verticle_slides.append(picture)

        return verticle_slides

    def get_most_similar_arr(self, picture):
        for picture_comparison in self.pictures:
            if picture.id == picture_comparison.id:
                continue
            else:
                print("TODO: Implement later")

    def get_best_vertical_match(self, picture, pictures_copy):
        picture_match = None
        for i in range(len(pictures_copy) - 1):
            if pictures_copy[i].orientation == "V":
                picture_match = i
        return picture_match



    def sortVerticalsByDifficulty(self):
        my_verticle_slides = self.createVerticalList()
        vertical_slides_difficulty = []

        for i in range(len(my_verticle_slides)):
            first_slide = my_verticle_slides[i]
            total_difficulty_score = 0
            for j in range(len(my_verticle_slides)):
                second_slide = my_verticle_slides[j]
                if first_slide.id != second_slide.id:
                    difficulty_score = self.get_difficulty_score(first_slide, second_slide)
                    total_difficulty_score += difficulty_score
            difficulty_arr = [first_slide.id, total_difficulty_score]
            vertical_slides_difficulty.append(difficulty_arr)

        vertical_slides_difficulty.sort(reverse=False, key=self.sortCriteria)
        return vertical_slides_difficulty

    def sortCriteria(self, difficultyArr):
        return difficultyArr[1]

    def get_difficulty_score(self, slide1, slide2):
        difficulty = slide1.get_overlap_details(slide2)
        difficulty_score = (difficulty['different'] - difficulty['same']) * -1
        return difficulty_score

    def add_slide(self, slide):
        self.slides.append(slide)

    def get_num_slides(self):
        return len(self.slides)

    def get_slide_ids(self):
        slide_ids = []
        for slide in self.slides:
            slide_ids.append(slide.id)
        return slide_ids

    def get_score(self):
        score = 0
        for i in range(0, len(self.slides) - 1):
            score += self.slides[i].get_score(self.slides[i + 1])
        score += self.slides[len(self.slides) - 1].get_score(self.slides[0])
        return score