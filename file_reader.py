import os


def read_file(file):

    with open(file, 'r') as i:
        lines = i.readlines()

    count = 0
    header = 0
    rows = []
    for line in lines:
        line = line.replace('\n', '')
        line_arr = line.split(' ')
        if count == 0:
            header = int(float(line_arr[0]))
        else:
            slide = {'orientation': line_arr[0], 'tags_length': int(float(line_arr[1])), 'tags': [], 'id': count-1}
            for i in range(2,len(line_arr)):
                slide['tags'].append(line_arr[i])
            rows.append(slide)
        count += 1

    return {'header': header, 'rows': rows}
