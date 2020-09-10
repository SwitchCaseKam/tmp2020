def get_words_equals_numbers_from_file(file_name):
    with open(file_name, 'r') as input_file:
        file_content = input_file.readlines()
        words_equals_numbers = []
        for line in file_content:
            number = int(line.split(' ')[0])
            word = line.split(' ')[1].strip()
            if number == len(word):
                words_equals_numbers.append([number, word])
        return words_equals_numbers

def get_lower_pair(pair1, pair2):
    pair_1 = [pair1[0], pair1[1]]
    pair_2 = [pair2[0], pair2[1]]

    if pair_1[0] < pair_2[0]:
        return pair_1
    elif pair_1[0] > pair_2[0]:
        return pair_2
    else:
        word_len = min([pair_1[1], pair_2[1]], key=len)
        for i in range(0, len(word_len)):
            if pair_1[1][i] < pair_2[1][i]:
                return pair_1
            elif pair_1[1][i] > pair_2[1][i]:
                return pair_2
            else:
                continue
        return pair_1


words_equals_numbers = get_words_equals_numbers_from_file('pary.txt')
lower_pair = words_equals_numbers[0]
for i in range(0, len(words_equals_numbers)-1):
    lower_pair = get_lower_pair(lower_pair, words_equals_numbers[i+1])
print(lower_pair)



