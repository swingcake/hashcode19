class Slide:
    def __init__(self, picture_one, picture_two=None):
        self.id = str(picture_one.id)
        self.pictures = [picture_one, picture_two]
        if picture_two is not None:
            self.id += " {}".format(str(picture_two.id))
        self.tags = {}
        for tag in picture_one.tags:
            self.tags[tag] = True
        if picture_two is not None:
            for tag in picture_two.tags:
                self.tags[tag] = True

    def get_num_tags(self):
        return len(self.tags)

    def get_tags_arr(self):
        return list(self.tags.values())

    def get_tags_obj(self):
        return self.tags

    def get_score(self, slide):
        overlap_details = self.get_overlap_details(slide)
        same = overlap_details['same']
        return min(self.get_num_tags() - same, same, slide.get_num_tags() - same)

    def get_overlap_details(self, other_slide):
        same_tags_count = 0
        different_tags_count = 0
        other_slide_tags = other_slide.get_tags_arr()
        for tag in other_slide_tags:
            if tag in self.tags:
                same_tags_count += 1
            else:
                different_tags_count += 1
        for tag in self.get_tags_arr():
            if tag not in other_slide_tags:
                different_tags_count += 1

        return {'same': same_tags_count, 'different': different_tags_count}
