from PIL import Image

mac = Image.open('example.jpg')

print(type(mac))
print(mac.filename)
print(mac.format_description)
print(mac.size)
mac.show()


## Cropping Images

new_image = mac.crop((0,0,100,100))
new_image.show()

print('-----------------------------')
pencils = Image.open("pencils.jpg")
pencils.show()
print(pencils.size)

# Cropping to only get the first three pencils

x = 0   # Starting X Coordinate
y = 0   # Starting Y coordinate

w = 1950 / 3    # 30% of the height
h = 1300 / 10 # 10% percent

three_pencils = pencils.crop((x,y,w,h))
three_pencils.show()

print('-----------------------------')
# Lets grab the last three pencils now

x = 0
y = 1100

w = 1950 / 3
h = 1300

last_pencils = pencils.crop((x,y,w,h))
print(last_pencils.size)
last_pencils.show()

print('-----------------------------')
# Lets get just the Mac computer

print(mac.size)

halfway = 1993 / 2

x = halfway - 200
w = halfway + 200

y = 800
h = 1257

mac_computer = mac.crop((x,y,w,h))
mac_computer.show()


print('-----------------------------')
# Lets copy and paste the cropped image into the original mac image

mac.paste(im=mac_computer,box=(0,0))
mac.paste(im=mac_computer,box=(796,0))
mac.show()

print('-----------------------------')
# Lets resize an image

resized = mac.resize((3000,500))
resized.show()

print('-----------------------------')
# Lets rotate an image

rotated = mac.rotate(90)
rotated.show()

print('-----------------------------')
# Working with transparency in images

red = Image.open("red_color.jpg")
blue = Image.open("blue_color.png")

blue.putalpha(0)    # Makes image fully transparent
blue.show()

blue.putalpha(128)    # Makes slightly transparent
blue.show()

red.putalpha(128)    # Makes slightly transparent
red.show()


print('-----------------------------')
# Paste transparent image ontop of other transparent image
blue.paste(im=red,box=(796,0),mask=red)
blue.show()