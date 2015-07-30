from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("img.jpg")
(width, height) = img.size
print width, height
draw = ImageDraw.Draw(img)
#font = ImageFont.truetype('Ubuntu-BI.ttf', 16)
#font = ImageFont.truetype("arial.ttf", 64)
#font = ImageFont.truetype('arial', 20)

draw.text((width - 80,0), "Sample Text", (255,0,0))
img.save('Sampleout.jpg')