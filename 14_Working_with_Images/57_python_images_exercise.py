from PIL import Image

word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print(word_matrix.size)
mask = mask.resize((1015, 559))
mask.putalpha(200)

word_matrix.paste(mask,(0,0), mask)
word_matrix.show()