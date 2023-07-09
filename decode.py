#!/usr/bin/python

import os, sys
from PIL import Image
from utils import rgb_to_binary


def main():
        img_path = 'encoded.png'
        output_path = 'Decrypt'
        filename, file_ext = os.path.splitext(output_path)
        output_path = filename + '.png'
        decoded_image = decode(Image.open(img_path))
        decoded_image.save(output_path)
def extract_hidden_pixels(image, width_visible, height_visible, pixel_count):
        hidden_image_pixels = ''
        idx = 0
        for col in range(width_visible):
            for row in range(height_visible):
                if row == 0 and col == 0:
                    continue
                r, g, b = image[col, row]
                r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
                hidden_image_pixels += r_binary[4:8] + g_binary[4:8] + b_binary[4:8]
                if idx >= pixel_count * 2:
                    break
                idx += 1
        return hidden_image_pixels


def reconstruct_image(image_pixels, width, height):
        image = Image.new("RGB", (width, height))
        image_copy = image.load()
        idx = 0
        for col in range(width):
            for row in range(height):
                r_binary = image_pixels[idx:idx + 8]
                g_binary = image_pixels[idx + 8:idx + 16]
                b_binary = image_pixels[idx + 16:idx + 24]
                if len(r_binary) >= 8 and len(g_binary) >= 8 and len(b_binary) >= 8:
                    image_copy[col, row] = (int(r_binary, 2), int(g_binary, 2), int(b_binary, 2))
                    idx += 24
        return image


def decode(image):
    image_copy = image.load()
    width_visible, height_visible = image.size
    r, g, b = image_copy[0, 0]
    r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
    w_h_binary = r_binary + g_binary + b_binary
    width_hidden = int(w_h_binary[0:12], 2)
    height_hidden = int(w_h_binary[12:24], 2)
    pixel_count = width_hidden * height_hidden
    hidden_image_pixels = extract_hidden_pixels(image_copy, width_visible, height_visible, pixel_count)
    decoded_image = reconstruct_image(hidden_image_pixels, width_hidden, height_hidden)
    return decoded_image


if __name__ == '__main__':
    main()

# #!/usr/bin/python
#
# import os, sys
# from PIL import Image
# from utils import rgb_to_binary
#
# def main():
#     encoded_image_path = 'infosecproject.png'
#     hidden_image_path = 'pngwing.com (9).png'
#     output_path = 'decrypted_image.png'
#     encoded_image = Image.open(encoded_image_path)
#     hidden_image = Image.open(hidden_image_path)
#     decoded_image = decode(encoded_image, hidden_image)
#     decoded_image.save(output_path)
#
# def decode(encoded_image, hidden_image):
#     encoded_image_copy = encoded_image.copy()
#     hidden_image_copy = hidden_image.copy().load()
#     width_encoded, height_encoded = encoded_image_copy.size
#     width_hidden, height_hidden = hidden_image.size
#     hidden_image_pixels = extract_hidden_pixels(hidden_image_copy, width_hidden, height_hidden)
#
#     idx = 0
#     for col in range(width_encoded):
#         for row in range(height_encoded):
#             if row == 0 and col == 0:
#                 continue
#             r, g, b = encoded_image_copy.getpixel((col, row))
#             r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#             r_binary_hidden = hidden_image_pixels[idx][0][-4:]
#             g_binary_hidden = hidden_image_pixels[idx][1][-4:]
#             b_binary_hidden = hidden_image_pixels[idx][2][-4:]
#             r_binary_new = r_binary[0:4] + r_binary_hidden
#             g_binary_new = g_binary[0:4] + g_binary_hidden
#             b_binary_new = b_binary[0:4] + b_binary_hidden
#             idx += 1
#             if idx >= len(hidden_image_pixels):
#                 decoded_image = Image.new("RGB", (col + 1, row + 1))
#                 decoded_image.putpixel((col, row), (int(r_binary_new, 2), int(g_binary_new, 2), int(b_binary_new, 2)))
#                 return decoded_image
#             encoded_image_copy.putpixel((col, row), (int(r_binary_new, 2), int(g_binary_new, 2), int(b_binary_new, 2)))
#     return None
#
# def extract_hidden_pixels(image, width, height):
#     hidden_image_pixels = []
#     for col in range(width):
#         for row in range(height):
#             pixel = image[col, row]
#             r = pixel[0]
#             g = pixel[1]
#             b = pixel[2]
#             r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#             hidden_image_pixels.append((r_binary, g_binary, b_binary))
#     return hidden_image_pixels
#
# def extract_hidden_pixels(image, width_hidden, height_hidden):
#     hidden_image_pixels = ''
#     idx = 0
#     for col in range(width_hidden):
#         for row in range(height_hidden):
#             r, g, b = image[col, row]
#             r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#             hidden_image_pixels += r_binary[4:8] + g_binary[4:8] + b_binary[4:8]
#     return hidden_image_pixels
#
# def reconstruct_image(image_pixels, width, height):
#     image = Image.new("RGB", (width, height))
#     image_copy = image.load()
#     idx = 0
#     for col in range(width):
#         for row in range(height):
#             r_binary = image_pixels[idx:idx+8]
#             g_binary = image_pixels[idx+8:idx+16]
#             b_binary = image_pixels[idx+16:idx+24]
#             image_copy[col, row] = (int(r_binary, 2), int(g_binary, 2), int(b_binary, 2))
#             idx += 24
#     return image
#
# def decode(encoded_image, hidden_image):
#         width_hidden, height_hidden = hidden_image.size
#         width_encoded, height_encoded = encoded_image.size
#         hidden_image_pixels = extract_hidden_pixels(hidden_image, width_hidden, height_hidden)
#         decoded_image = Image.new('RGB', (width_hidden, height_hidden))
#         decoded_image_copy = decoded_image.load()
#         idx = 0
#         for col in range(width_encoded):
#             for row in range(height_encoded):
#                 if row == 0 and col == 0:
#                     continue
#                 r, g, b = encoded_image[col, row]
#                 r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#                 r_hidden = hidden_image_pixels[col][row][0:4] + r_binary[4:]
#                 g_hidden = hidden_image_pixels[col][row][4:8] + g_binary[4:]
#                 b_hidden = hidden_image_pixels[col][row][8:12] + b_binary[4:]
#                 decoded_image_copy[col, row] = (int(r_hidden, 2), int(g_hidden, 2), int(b_hidden, 2))
#                 idx += 12
#                 if idx >= width_hidden * height_hidden * 3:
#                     return decoded_image
#         # can never be reached, but let's return the image anyway
#         return decoded_image
#
#
# if __name__ == '__main__':
#     main()
#
# import os, sys
# from PIL import Image
# from utils import rgb_to_binary
#
# def main():
#     encoded_image_path = 'infosecproject.png'
#     hidden_image_path = 'pngwing.com (9).png'
#     output_path = 'decrypted_image.png'
#     encoded_image = Image.open(encoded_image_path)
#     hidden_image = Image.open(hidden_image_path)
#     decoded_image = decode(encoded_image, hidden_image)
#     decoded_image.save(output_path)
#
# def decode(encoded_image, hidden_image):
#     encoded_image_copy = encoded_image.copy()
#     hidden_image_copy = hidden_image.copy().load()
#     width_encoded, height_encoded = encoded_image_copy.size
#     width_hidden, height_hidden = hidden_image.size
#     hidden_image_pixels = extract_hidden_pixels(hidden_image_copy, width_hidden, height_hidden)
#
#     print("Number of hidden pixels extracted:", len(hidden_image_pixels))
#
#     idx = 0
#     for col in range(width_encoded):
#         for row in range(height_encoded):
#             if row == 0 and col == 0:
#                 continue
#             r, g, b = encoded_image_copy.getpixel((col, row))
#             r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#             r_binary_hidden = hidden_image_pixels[idx][0][-4:]
#             g_binary_hidden = hidden_image_pixels[idx][1][-4:]
#             b_binary_hidden = hidden_image_pixels[idx][2][-4:]
#             r_binary_new = r_binary[0:4] + r_binary_hidden
#             g_binary_new = g_binary[0:4] + g_binary_hidden
#             b_binary_new = b_binary[0:4] + b_binary_hidden
#             idx += 1
#
#             print("idx:", idx)
#             print("len(hidden_image_pixels):", len(hidden_image_pixels))
#
#             if idx >= len(hidden_image_pixels):
#                 decoded_image = Image.new("RGB", (col + 1, row + 1))
#                 decoded_image.putpixel((col, row), (int(r_binary_new, 2), int(g_binary_new, 2), int(b_binary_new, 2)))
#                 return decoded_image
#             encoded_image_copy.putpixel((col, row), (int(r_binary_new, 2), int(g_binary_new, 2), int(b_binary_new, 2)))
#
#     return None
#
# def extract_hidden_pixels(image, width, height):
#     hidden_image_pixels = []
#     for col in range(width):
#         for row in range(height):
#             pixel = image[col, row]
#             r = pixel[0]
#             g = pixel[1]
#             b = pixel[2]
#             r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#             hidden_image_pixels.append((r_binary, g_binary, b_binary))
#     return hidden_image_pixels
#
# if __name__ == '__main__':
#     main()

# !/usr/bin/python

# import os, sys
# from PIL import Image
# from utils import rgb_to_binary
#
#
# def main():
#         img_path = 'infosecproject.png'
#         output_path = 'abc'
#         filename, file_ext = os.path.splitext(output_path)
#         output_path = filename + '.png'
#         decoded_image = decode(Image.open(img_path))
#         decoded_image.save(output_path)
#
#
# def extract_hidden_pixels(image, width_visible, height_visible, pixel_count):
#     hidden_image_pixels = ''
#     idx = 0
#     for col in range(width_visible):
#         for row in range(height_visible):
#             if row == 0 and col == 0:
#                 continue
#             r, g, b = image.getpixel((col, row))
#             r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#             hidden_image_pixels += r_binary[4:8] + g_binary[4:8] + b_binary[4:8]
#             if idx >= pixel_count * 2:
#                 return hidden_image_pixels
#     return hidden_image_pixels
#
#
# def reconstruct_image(image_pixels, width, height):
#     image = Image.new("RGB", (width, height))
#     image_copy = image.load()
#     idx = 0
#     for col in range(width):
#         for row in range(height):
#             r_binary = image_pixels[idx:idx + 8]
#             g_binary = image_pixels[idx + 8:idx + 16]
#             b_binary = image_pixels[idx + 16:idx + 24]
#             image_copy[col, row] = (int(r_binary, 2), int(g_binary, 2), int(b_binary, 2))
#             idx += 24
#     return image
#
#
# def decode(image):
#     image_copy = image.load()
#     width_visible, height_visible = image.size
#     r, g, b = image_copy[0, 0]
#     r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
#     w_h_binary = r_binary + g_binary + b_binary
#     width_hidden = int(w_h_binary[0:12], 2)
#     height_hidden = int(w_h_binary[12:24], 2)
#     pixel_count = width_hidden * height_hidden
#     hidden_image_pixels = extract_hidden_pixels(image, width_visible, height_visible, pixel_count)
#     decoded_image = reconstruct_image(hidden_image_pixels, width_hidden, height_hidden)
#     return decoded_image
#
#
# if __name__ == '__main__':
#     main()
