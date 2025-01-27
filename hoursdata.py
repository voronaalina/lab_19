import shelve

workers_hours = {
    "Багряний": 12,
    "Савелюк": 9,
    "Демченко": 8,
    "Симоненко": 10,
    "Куліш": 11,
    "Винниченко": 5,
    "Петлюра": 7,
    "Грушевський": 8,
    "Герасименко": 9,
    "Левицький": 4,
    "Тютюнник": 9,
    "Карпенко": 10,
    "Вишня": 14,
    "Журавель": 5,
    "Коцюбинський": 9,
    "Костомаров": 3,
    "Петрушевич": 10,
    "Довженко": 7
}

with shelve.open('workers_hours') as db:
    db['workers']=workers_hours
print("дані збережені у 'workers_hours'.")
