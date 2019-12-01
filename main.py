
import json
import xml
import xml.etree.ElementTree as ET
from pprint import pprint

def read_json(newsafr=None): # Чтение из Json
    with open('newsafr.json', encoding='utf-8') as js:
        json_data = json.load(js)
        articles = json_data['rss']['channel']['items']
        list_description = []
        for news in articles:
            list_articles = news['description'].split(" ")
            for word in list_articles:
                list_description.append(word.lower())
    make_dict(list_description, "json")

def read_xml(): # Чтение данных из .xml
    tree = ET.parse('./newsafr.xml')
    root = tree.getroot()
    descriptions = root.findall('channel/item/description')
    list_description = []
    for descr in descriptions:
        for word in descr.text.split(" "):
            list_description.append(word.lower())
    make_dict(list_description, "xml")

def make_dict(data, file_type): # Создание словаря со словами и количеством их повторений
    count_words = {}
    for word in data:
        if len(word) > 6:
            if word in count_words.keys():
                count_words[word] += 1
            else:
                count_words[word] = 1
    top_words(count_words, file_type)

def top_words(count_words, file_type): # Сотировка и вывод 10 наиболее часто встречающихся слов
    count_words_key = count_words.keys()
    count_words_value = count_words.values()
    top = sorted(zip(count_words_value, count_words_key), reverse=True)
    print(f"\nТоп-10 самых популярных слов в новостях файла .{file_type}:")
    for value in top[0:10:1]:
        print(f"Слово '{value[1]}' встречается в тексте новости: {value[0]} раз(а).")


read_json()
read_xml()