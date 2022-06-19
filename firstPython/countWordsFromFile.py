def countWordsFromFile():
    file_name = input('Enter the file name: ')
    number_of_words = 0
    file = open(file_name, 'r')
    for line in file:
        words = line.split()
        number_of_words = number_of_words+ len(words)

    print('Number of words: ', number_of_words)

countWordsFromFile()