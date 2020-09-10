def find_prime_numbers(number):
    prime_numbers = [];
    for i in range(2, number):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


def get_even_numbers_from_file(file_name):
    with open(file_name, 'r') as input_file:
        file_content = input_file.readlines()
        even_numbers = []
        for line in file_content:
            number = int(line.split(' ')[0])
            if (number % 2) == 0:
                even_numbers.append(number)
    return even_numbers

even_numbers = get_even_numbers_from_file('pary.txt')
for evenNumber in even_numbers:
    prime_numbers = find_prime_numbers(evenNumber);
    elements = set([])
    for i in prime_numbers:
        for j in prime_numbers:
            if (i + j) == evenNumber:
                elements.add(i)
                elements.add(j)
    print(str(evenNumber), min(elements), max(elements))

