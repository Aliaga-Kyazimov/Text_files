file_1 = open('1.txt', 'rt+', encoding='utf-8')
file_2 = open('2.txt', 'rt+', encoding='utf-8')
file_3 = open('3.txt', 'rt+', encoding='utf-8')

num_of_lines = {}
all_files = [file_1, file_2, file_3]
for file in all_files:
    count = 0
    for line in file:
        count += 1
    num_of_lines[file.name] = count

sorted_dict = {}
sorted_keys = list(sorted(num_of_lines, key=num_of_lines.get))
for key in sorted_keys:
    sorted_dict[key] = num_of_lines[key]

file_1.close()
file_2.close()
file_3.close()

file_1 = open('1.txt', 'rt+', encoding='utf-8')
file_2 = open('2.txt', 'rt+', encoding='utf-8')
file_3 = open('3.txt', 'rt+', encoding='utf-8')

for k, v in sorted_dict.items():
    print(f'{k}\n{v}')
    if k == file_1.name:
        print(file_1.read())
    elif k == file_2.name:
        print(file_2.read())
    else:
        print(file_3.read())

file_1.close()
file_2.close()
file_3.close()