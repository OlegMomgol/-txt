with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines_text = len(lines)

words_text = 0
line_2 = ""

for line in lines:
    words = line.split()
    words_text += len(words)
    if len(line) > len(line_2):
        line_2 = line.strip()


print(f'Общее количество слов: {words_text}')
print(f'Общее количество строк: {lines_text}')
print(f'Самая длинная строка: "{line_2}" (длина: {len(line_2)})')
