import csv
import os
import json

def get_data():
    path = os.path.abspath("./movies_metadata.csv")
    file = open(path, encoding='utf-8', newline='', errors='ignore')
    reader = csv.DictReader(file)
    datas = []  # moi data bao gom [pos,title,genre,language,avr,overviews]
    pos = 0

    for line in reader:
        pos += 1  
        g = []          # g  luu tat ca cac the loai cua 1 bo phim
        s = line['genres'].replace('\'', '\"')  
        s = json.loads(s)
        for each in s:
            g.append(each['name'])      #append ten the loai vao g

        string_genre = ' '.join(g)      #bien tat ca cac the loai thanh 1 string

        datas.append([pos, line['original_title'], string_genre,
                    line['original_language'], line['vote_average'],line['overview']])
    return datas
