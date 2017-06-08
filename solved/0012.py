
import Image, ImageEnhance
im = Image.open('evil1.jpg', 'r')
final=ImageEnhance.Brightness(im)
final.enhance(4).save("evil2.jpeg", "JPEG")