from data_analysis import get_data
datas = get_data()
def search(keyword=None, genre=None, language=None, howmany=None):
    if genre == '--':
        genre = ''
    if language == '--':
        language = ''
        
    title_score = []    #moi gia tri gom [title,avr,overview]
    for x in datas:
        if keyword.lower() in x[1].lower():
            if genre in x[2]:
                if language[:2] in x[3]:
                    title_score.append([x[1], x[4],x[5]])

    #sap xep theo diem giam dan
    title_score = sorted(title_score, key=lambda x: x[1], reverse=True)
    
    #show ra thu tu phim ma nguoi dung expect
    if howmany == 1:
        tmp_res = title_score[:10]
        return tmp_res
    if howmany == 2:
        tmp_res = title_score[:5]
        return tmp_res
    if howmany == 3:
        tmp_res = title_score
        return tmp_res