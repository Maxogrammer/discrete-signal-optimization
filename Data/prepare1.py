'''
Преобразовывает опыт (Exp) в вид, удобный для использования (.json).
Изначально должен уметь преобразовывать собранные нами .txt в .json, а именно:
	а) создавать файлы, где каждая деятельность указана в хронологическом порядке — chr
	б) создавать файлы, где найдена сумма каждой деятельности в каждом цикле — int
'''

from json import dump
from os import path as ospath

def prepare(data):
    current_directory = ospath.dirname(__file__)
    prep_data_path = ospath.join(current_directory, 'PreparedExp', f'Phone1.json')
    prep_data = open(prep_data_path, "w")

    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    buk = ["в", "м", "о", "з"]
    result = []
    def jjoin(para, num, buk):
        void = ""
        void1 = ""
        for el in para:
            if el in num:
                void = "a"
        if void == "":
            return para
        if void == "a":
            void = ""
        for x in para:
            if x in num:
                void = void + x
            if x in buk:
                if x == "о":
                    void1 = "O"
                if x == "з":
                    void1 = "I"
                if x == "м":
                    void1 = "@"
                if x == "в":
                    void1 = "&"
        para = []
        para.append(int(void))
        para.append(void1)
        line_list.append(para)
    for line in data:
        line_list = []
        para = []
        for el in line:
            prob = 0
            if el in num:
                para.append(el)
            if el in buk:
                para.append(el)
            if el == " ":
                prob += 1
                jjoin(para, num, buk)
                para = []
            if el == "\n":
                pass
        if prob == 0:
            jjoin(para, num, buk)
            para = []
        para.append(line_list[0][0])
        para.append(line_list[1][0])
        line_list[0] = para
        line_list.pop(1)
        result.append(line_list)
    dump(result, prep_data)
    prep_data.close()
