def search_element(data, tag, index):
    result = None
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag,index)
            for i,ind in enumerate(result):
                if i == index:
                    print(data(ind))
            if result:
                return result
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search_key = input("Искомый ключ: ")

index = int(input('введите глубину жлемента'))

value = search_element(site, search_key, index)
if value:
    print("Значение:", value)
else:
    print("Такого ключа в структуре сайта нет.")