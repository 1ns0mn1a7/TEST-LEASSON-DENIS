from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
coordinates = 50, 0, image.width, image.height
red_cropped = red.crop(coordinates)
coordinates1 = 25, 0, 671, 522
red_cropped1 = red.crop(coordinates1)
coordinates2 = 0, 0, 646, 522
blue_cropped = blue.crop(coordinates2)
blue_cropped1 = blue.crop(coordinates1)
red_blended = Image.blend(red_cropped, red_cropped1, 0.5)
blue_blended = Image.blend(blue_cropped, blue_cropped, 0.5)
green_cropped = green.crop(coordinates1)
monro_3d = Image.merge("RGB", (red_blended, green_cropped, blue_blended))
monro_3d.thumbnail((80, 80))
monro_3d.save("monro_3d.jpg")