def create_index(input_file, output_file):
    index = {}
    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, 1):
            words = line.strip().split()
            for word in words:
                word = word.strip(',.:;?!')
                if word not in index:
                    index[word] = [line_number]
                else:
                    index[word].append(line_number)

    with open(output_file, 'w') as index_file:
        for word in sorted(index):
            index_file.write(f"{word}: {' '.join(map(str, index[word]))}\n")

create_index("Kennedy.txt", "Index.txt")
