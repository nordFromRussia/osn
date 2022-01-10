from PIL import Image
im = Image.open('йцу.jpg')
pixels = im.load()  # список с пикселями
x, y = im.size
print(pixels)
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = r, 0, 0
im.save('res.png')