def parser_text(file_path):
    words_dict = {}
    with open (file_path, 'r', encoding='utf-8') as file:
        for line in file:
            split_line = line.strip().split('\t')
            for single_line in split_line[0].split(';'):
                word_foreign = single_line.strip()
                word_translation = split_line[1].strip().split(';')
                words_dict[word_foreign] = word_translation
        return words_dict

def list_foreign_traslate(words_dict):
    list_foreign_word = []
    list_translation_word = []
    for key,values in words_dict.items():
        for value in values:
            list_foreign_word.append(key)
            list_translation_word.append(value)
    return list_foreign_word, list_translation_word

def write(file_path, items):
    with open(file_path, 'w', encoding="utf-8") as file:
        for word in items:
            file.write(f'{word}\n')

def main():
    try:
        words_dict = parser_text('PythonTest.txt')
    except FileNotFoundError:
        print('Error')
    else:
        list_foreign_word, list_translation_word = list_foreign_traslate(words_dict)
        write('Russian.txt', list_translation_word)
        write('English.txt', list_foreign_word)
        print('Ready')

if __name__ == '__main__':
    main()
