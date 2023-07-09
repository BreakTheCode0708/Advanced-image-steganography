# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from PIL import Image
def Encode(img, msg, lst):
    global L
    L = []
    length=len(msg)
    if length > 255:
        print("Text too long! (don't exeed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("Image mode needs to be RGB")
        return False
    # Making deep copy of image to make encryption! with original image intact
    encoded_img = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = lst[index - 1]
                asc = c // 255
                # Storing remainder value, used for decoding
                L += [c % 255]
            else:
                asc = r
            encoded_img.putpixel((col, row), (asc, g, b))
            index += 1
    return encoded_img


# Decode function of Steganography

def Decode(img):
    global L
    width, height = img.size
    msg = ""
    lst = []
    index = 0
    length = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                lst += [r * 255 + L[index-1]]
            index += 1
    return lst
