# Задача "Найдёт везде".

# Написать класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченное количество названий файлов
# и записывать их в атрибут file_names в виде списка или кортежа.

# Объект класса WordsFinder должен обладать следующими методами:
# 1. get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}

# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

# 2. find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - позиция первого такого слова в списке слов этого файла.

# 3. count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.

# В методах find и count пользоваться ранее написанным методом get_all_words.

class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = []
                for j in file:
                    for k in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                        j = j.replace(k, '')
                    words.extend(j.lower().split())
                    all_words[i] = words
        return all_words

    def find(self, word):
        found = {}
        for i, j in self.get_all_words().items():
            for k in j:
                if word.lower() == k:
                    index = j.index(k) + 1
                    found[i] = index
        return found

    def count(self, word):
        counted = {}
        for i, j in self.get_all_words().items():
            counter = 0
            for k in j:
                if word.lower() == k:
                    counter += 1
                    counted[i] = counter
        return counted

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))