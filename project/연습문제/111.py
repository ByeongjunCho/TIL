students = {
    'ㅁㄴㅇㄹ1': {
        '순번': '01',
        '이름': '김성훈'
    },
    'ㅁㄴㅇㄹ2': {
        '순번': '02',
        '이름': '김은정'
    }
}

with open('c.csv', 'w', encoding='utf-8') as f:
    f.write('number, name\n')
    for number, name in students.items():
        f.write(f'{number}, {name}\n')
