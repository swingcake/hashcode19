class Picture:
    def __init__(self, data):
        self.orientation = data['orientation']
        self.tags_length = data['tags_length']
        self.tags = data['tags']
        self.id = data['id']
        self.tags = {}
        for tag in data['tags']:
            self.tags[tag] = True

    def get_tags_arr(self):
        return list(self.tags.keys())

    def get_overlap_details(self, other_picture):
        same_tags_count = 0
        different_tags_count = 0
        other_picture_tags = other_picture.get_tags_arr()
        for tag in other_picture_tags:
            if tag in self.tags:
                same_tags_count += 1
            else:
                different_tags_count += 1
        for tag in self.get_tags_arr():
            if tag not in other_picture_tags:
                different_tags_count += 1

        return {'same': same_tags_count, 'different': different_tags_count}
