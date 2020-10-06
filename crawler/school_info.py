import openpyxl
import json
from tqdm import tqdm

def convert_to_json():
    # 엑셀파일 열기
    wb = openpyxl.load_workbook('data/고등학교 목록.xlsx')

    # 현재 Active Sheet 얻기
    ws = wb.active

    # 국영수 점수를 읽기
    high_school_data = {}
    for r in tqdm(ws.rows):
        if r[0].row  < 5 or r[1].value != '고등학교':
            continue

        if r[6].value not in high_school_data:
            high_school_data[r[6].value] = []

        high_school_data[r[6].value].append({
            "region" : r[4].value,
            "subRegion" : r[5].value,
            "eduInstit" : r[6].value,
            "name" : r[7].value,
            "type" : r[2].value,
            "type2" : r[3].value,
            "foundation" : r[10].value,
            "gender" : r[11].value,
            "postNum" : r[12].value,
            "address" : r[13].value,
            "contact" : r[14].value,
            "fax" : r[15].value,
            "homePage" : r[16].value,
        })
    return high_school_data

def save_json(file_name, json_data):
    with open(file_name+'.json', "w", encoding = 'utf8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


def read_json(file_name):
    json_data = {}

    with open(file_name, encoding = 'utf8') as json_file:
        json_data = json.load(json_file)

    return json_data

def compare(list_one, list_two):
    names = []
    for school in list_one:
        if not any(list(map(lambda x: x['name'] == school['name'], list_two))):
            names.append(school['name'])
    return names

def analyze():
    name_convert = {'충북' : '충청북도', '충남' : '충청남도', '전북':'전라북도', '전남':'전라남도', '경북':'경상북도', '경남':'경상남도'}
    schools_one = read_json('data/school_list.json')
    schools_two = read_json('data/school_info.json')

    total_info_school = 0
    total_cafe_school = 0
    total_not_info_school = 0
    total_not_cafe_school = 0

    for city, schools in schools_two.items():
        for insti in schools_one.keys():
            nickname = name_convert[city] if city in name_convert else city[:2]
            if nickname in insti:
                only_in_info = compare(schools, schools_one[insti])
                only_in_list = compare(schools_one[insti], schools)
                print(insti, "자세한 학교 정보가 지원되는 학교 개수 :" + str(len(schools)),
                "급식 정보가 지원 되는 학교 개수 :"+str(len(schools_one[insti])), sep='\n')
                print()
                print('학교 정보만 지원되는 학교 :', len(only_in_info))
                for name in only_in_info:
                    print(name)
                print()
                print('급식 정보만 지원되는 학교 :', len(only_in_list))
                for name in only_in_list:
                    print(name)
                print()

                total_info_school += len(schools)
                total_cafe_school += len(schools_one[insti])
                total_not_info_school += len(only_in_list)
                total_not_cafe_school += len(only_in_info)

    print("info", total_info_school, f"({round((total_info_school-total_not_cafe_school)/total_info_school * 100, 3)})")
    print("cafe", total_cafe_school, f"({round((total_cafe_school-total_not_info_school)/total_cafe_school * 100, 3)})")
    print("not support info", total_not_info_school)
    print("not support cafe", total_not_cafe_school)


if __name__ == '__main__':
    //analyze()