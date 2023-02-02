# Словарь - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up':       '^',
        'left':     '<',
        'down':     'v',
        'right':    '>'
    }

print(dictionary)           # {'up':'^', 'left':'<', 'down':'v', 'right':'>'}
print(dictionary['left'])   # <
                            # типы ключей могут различаться

for k in dictionary.keys():     # Ключи
    print(k)

for k in dictionary.values():   # Значения
    print(k)

del dictionary['left']          # Удаление элемента

for item in dictionary:
# for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
