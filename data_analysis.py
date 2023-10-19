import csv
import os
import json


def get_data():
    path = os.path.abspath("./movies_metadata.csv")
    file = open(path, encoding='utf-8', newline='', errors='ignore')
    reader = csv.DictReader(file)
    datas = []  # Each data include [pos,title,genre,language,avr,overviews]
    pos = 0

    for line in reader:
        pos += 1
        g = []  # Save all genres of a movie
        s = line['genres'].replace('\'', '\"')
        s = json.loads(s)
        for each in s:
            g.append(each['name'])  # Append each genre into g

        string_genre = ' '.join(g)  # Make all the genre become string

        # Save to datas
        datas.append([pos, line['original_title'], string_genre,
                      line['original_language'], line['vote_average'], line['overview']])
    return datas
