def get_words_from_file(file_name):
    with open(file_name, 'r') as input_file:
        file_content = input_file.readlines()
        words = []
        for line in file_content:
            word = line.split(' ')[1]
            words.append(word)
    return words

words = get_words_from_file('pary.txt')


for word in words:
    chars_sequence = ''
    chars_sequences_array = [word[0]]

    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            if chars_sequence == '':
                chars_sequence += word[i]
            chars_sequence += word[i+1]
        else:
            if chars_sequence != '':
                chars_sequences_array.append(chars_sequence)
            chars_sequence = ''

    print(max(chars_sequences_array, key=len), len(max(chars_sequences_array, key=len)))