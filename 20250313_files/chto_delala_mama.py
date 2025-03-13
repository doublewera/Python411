f = open('fairytale.txt', encoding='utf-8')  #, 'r', encoding='utf-8')
content = f.read(22)       # читаем первые 15 байт. Куда?
print(content)
storyend = f.read(9)        # читаем с текущего места и до конца
print(storyend)
f.close()