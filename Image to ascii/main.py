import pywhatkit as kit
# import pyautogui as gui
from PIL import Image, ImageDraw, ImageFont
art = kit.image_to_ascii_art(r"C:\Users\Black\OneDrive\Pictures\pics\player.png", r"C:\Users\Black\Videos\console_program\Image to ascii\gui")
# hand = kit.text_to_handwriting("Hello")
# gui.write(hand)
with open(r"C:\Users\Black\Videos\console_program\Image to ascii\gui.txt","r") as file:
    text = file.read()

img = Image.new("RGB",(800,600),(255,255,255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', size=5)
draw.text((50, 0), text, font=font, fill=(0, 0, 0))
img.show()
img.save('notepad_image.png')