# set the image no bigger than 200*150

from PIL import Image

img = Image.open('img.jpg')

out = img.resize((200,150), Image.ANTIALIAS)
out.save('resize.jpg')



