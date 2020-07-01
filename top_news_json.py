def read_files():
    '''
    Функция чтения файлов
    '''
    import json

    with open('/Users/konstantinsealov/Desktop/Python/HomeWork-DZ-8/py-homework-basic-files/newsafr.json', 'rb') as f:
        data = f.read()
        data = json.loads(data)
        original_text = ''

        for items in data['rss']['channel']['items']:
            original_text += ' ' + items['description']
        return original_text


def count_word(original_text):
    '''
    функция подсчета слов длиннее 6 символов
    '''
    to_list = original_text.split(' ')
    word_value = {}

    for word in to_list:
        if len(word) > 6:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value


def sort_top(word_value):
    '''
    функция сортировки и вывода ТОП-10
    '''

    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key=l, reverse=True)
    count = 1
    top_10 = {}

    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 11:
            break
    return top_10


def main():
    '''
    главная функция:  запускает другие функции
    '''

    print('Открытие файла ...')
    top_10 = sort_top(count_word(read_files()))

    for i in top_10.values():
        print(i[1], ' : ', i[0])

main()











