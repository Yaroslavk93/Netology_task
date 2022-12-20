queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

count_w = [len(i.split()) for i in queries]

for i in set(count_w):
    print(f'Поисковых запросов, содержащих {i} слов(а): '
          f'{round(count_w.count(i) * 100 / len(count_w), 2)}%')