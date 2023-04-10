import pdfplumber
import sys
import json

def get_filtered_text(file_to_parse: str) -> str:
    with pdfplumber.open(file_to_parse) as pdf:
        #text = pdf.pages[13]
        #clean_text = text.filter(lambda obj: not (obj["object_type"] == "char" and obj["size"] != 10))
        #print(clean_text.extract_text())

        w = -1

        for i in range(10,626):
            text = pdf.pages[i]
            if(text.filter(lambda obj: not (obj["object_type"] == "char" and obj["size"] != 18))):
                w += 1
                globals()[str(w)]={
                    'id': w,
                    '년도': 2022,
                    'title': (text.filter(lambda obj: not (obj["object_type"] == "char" and obj["size"] != 18))).extract_text(),
                    'contents': ""
                }

                if(globals()[str(w)]['title']==''):
                    globals()[str(w)]['title']= globals()[str(w-1)]['title']

            globals()[str(w)]['contents']+=(text.filter(lambda obj: not (obj["object_type"] == 1))).extract_text()


        for i in range(w+1):
            globals()[str(i)]['contents']=globals()[str(i)]['contents'].replace("\x00", ' ')
            print(globals()[str(i)])
            print('\n')

        with open('./data.json', 'w', encoding='utf-8') as f:
            for i in range(w+1):
                json.dump(globals()[str(i)], f, indent=4, ensure_ascii=False)

get_filtered_text("C:\ll.pdf")

