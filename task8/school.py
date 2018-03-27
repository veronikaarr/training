# coding=utf-8

"""Напиши скрипт который создает 2 сущности как учителя и ученики. Отношения многие ко многим.
 Есть классы - набор учеников. У каждого ученика кучу предметов и оценки за них…. найти учителей у которого самый
 самый лучший и худший класс по совокупности оценок. по предметам и оценкам за них… Посчитать время операции
 затрачиваемой на поиск… Проиндексировать так чтобы улучшить поиск.
1"""

from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.school
collection = db.school

"""Какой логикой я руководствовалась при выборе данной модели данных?
Ясно, что должны быть 2 модели - "учитель":
 teacher:
 { name,
 subj }
 и ещё одна, связывающая учителя с учениками/предметами.
Вторую модель можно реализовать 2мя способами: первый - модель "ученики", которая содержит 
в себе предметы и номер класса, второй - модель "предмет",
 pupil:
 { name,
 subj: {[ name,
        mark,
        teacher }, {}]
 class_id }
 второй - модель "предмет" содержит в себе класс и учителя, а класс содержит список учеников:
  subj:
  { name,
  class: [ { class_id:[{
                        pupil name,
                        mark}, {} ] },
            {} ],
  teacher}, } 
 На мой взгляд, обращение по запросу проще к второму виду модели: поиск по предмету, который ведёт учитель,
  подсчёт оценок для класса - школьники уже в него объединены. И добавляются гоораздо чаще класса, чем предметы,
  удаляются - ученики"""

teacher1 = [{ 't_name': 'Maria Ivanovna',
    'subject': 'physics',
    'age': 32 },
    {'t_name': 'Valentina Ivanovna',
    'subject': 'mathematics',
    'age': 32}]

subject1 = [{'s_name': 'physics',
            'class':[{'class_id': 1,
                      'pupil':
                          [{'pupil_name': 'Mother',
                           'mark': [5,4,3,2]},
                           {'pupil_name': 'Father',
                           'mark': [5,4,3,5]},
                           {'pupil_name': 'Grandmother',
                           'mark': [5,4,4,5]},
                           ]},
                     {'class_id': 2,
                      'pupil':
                          [{'pupil_name': 'Arina',
                            'mark': [5, 4, 3, 2]},
                           {'pupil_name': 'Vera',
                            'mark': [5, 4, 3, 5]},
                           {'pupil_name': 'Maksim',
                            'mark': [5, 4, 4, 5]},
                           ]}
                     ]},
{'s_name': 'mathematics',
            'class':[{'class_id': 1,
                      'pupil':
                          [{'pupil_name': 'Mother',
                           'mark': [5,4,3,2]},
                           {'pupil_name': 'Father',
                           'mark': [5,4,3,5]},
                           {'pupil_name': 'Grandmother',
                           'mark': [5,4,4,5]},
                           ]},
                     {'class_id': 2,
                      'pupil':
                          [{'pupil_name': 'Arina',
                            'mark': [5, 4, 3, 2]},
                           {'pupil_name': 'Vera',
                            'mark': [5, 4, 3, 5]},
                           {'pupil_name': 'Maksim',
                            'mark': [5, 4, 4, 5]},
                           ]}
                     ]}
]
'''result1 = db.teacher.insert(teacher1)
print(result1)
result2 = db.subject.insert(subject1)
print(result2)'''


