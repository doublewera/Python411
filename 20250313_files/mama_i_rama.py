f = open('fairytale.txt', 'w', encoding='utf-8')
f.write('Жила-была мама. Она мыла раму.')
# f.flush()
f.close()

f = open('fairytale.txt', 'a', encoding='utf-8')
f.write('Еще она мыла пол.')
# f.flush()
f.close()