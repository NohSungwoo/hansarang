import os
import re
from datetime import datetime, timedelta
from os.path import split

persons = {}
path = "./check24"


# 파일 개수 확인
def count_files(directory):
    all_items = os.listdir(directory)

    files = [f for f in all_items if os.path.isfile(os.path.join(directory, f))]

    return len(files)


files_count = count_files(path)


def read_file_bonus(day):
    with open(f"check24/{day}.txt", "r") as file:
        content = file.read()
        content = content.split("\n")
    return content


def read_file(day):
    with open(f"check24/{day}.txt", "r") as file:
        content = file.read()
        content = content.split()
    return content


def remove_date_and_space(content):
    # 첫 번째 열에 날짜 형식이 있는 경우에 날짜 형식을 제거
    if re.match(r"^\d{2}/\d{2}$", content[0]):
        names = content[1:]
    else:
        names = content

    if not names[0]:
        names.remove("")

    return names


def change_to_dict_attendance(names):
    for name in names:
        if len(name) == 3:
            name = name[1:]  # 성을 제거하고 이름만 사용
        else:
            name = name  # 이름이 두 글자인 경우 그대로 사용

        if not name.isdigit():
            # 기존 값이 있으면 1을 더하고, 없으면 1로 설정
            persons[name] = persons.get(name, 0) + 1

    return persons


persons_bonus = {}


def change_to_dict_bonus(names):
    for name in names:
        if len(name) > 4:
            name = name[1:]  # 성을 제거하고 이름만 사용
            split_name = name.split()
            key = split_name[0]
            value = int(split_name[1])

        if len(name) == 4:
            split_name = name.split()
            key = split_name[0]
            value = int(split_name[1])

            if key in persons_bonus:
                persons_bonus[key] += value
            else:
                persons_bonus[key] = value

    return persons_bonus


date = "0107"
date = datetime.strptime(date, "%m%d")
date = date.replace(year=2024)

for _ in range(files_count - 1):
    date = date + timedelta(days=7)
    md_date = date.strftime("%m%d")
    print(
        f"출석체크: {change_to_dict_attendance(remove_date_and_space(read_file(md_date)))}"
    )
    print(
        f"보너스 달란트{md_date}: {change_to_dict_bonus(remove_date_and_space(read_file_bonus(md_date)))}"
    )
