from PIL import Image
#ciel bleu foncé
image = Image.new('RGB', (10,10))
for i in range(0,10):
    for j in range(0,10):
        image.putpixel((i,j), (0, 1, 68))
#sable base + eau
for i in range(0,10):
    for j in range(7,10):
        image.putpixel((i,j), (204, 170, 0))
for i in range(0,3):
    image.putpixel((i,7), (0, 1, 68))
for i in range(8,10):
    image.putpixel((i,7), (0, 1, 68))
image.putpixel((4, 9), (183, 149, 0))
image.putpixel((6, 9), (183, 149, 0))
image.putpixel((0, 8), (46, 136, 201))
image.putpixel((9, 8), (46, 136, 201))
#palmier
for i in range(6,10):
      for j in range(2,5):
        image.putpixel((i, j), (12, 159, 6))
image.putpixel((4,3), (12, 159, 6))
image.putpixel((5,2), (12, 159, 6))
for i in range(6,9):
    image.putpixel((6,i), (144, 87, 0))
image.putpixel((7,4), (144, 87, 0))
image.putpixel((7,5), (144, 87, 0))
image.putpixel((8,4), (0, 1, 68))
#lune
for i in range(1,3):
    for j in range(0,2):
        image.putpixel((i, j), (181, 175, 175))
image.putpixel((1, 0), (148, 145, 145))
#étoiles
image.putpixel((0,4), (250, 255, 191))
image.putpixel((7,0), (250, 255, 191))
image.putpixel((9,6), (250, 255, 191))
#noix de coco
image.putpixel((4,8), (75, 32, 0))
image.putpixel((8,3), (75, 32, 0))
image.save("image.png")