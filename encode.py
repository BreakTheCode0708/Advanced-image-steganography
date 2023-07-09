#!/usr/bin/python

import os, sys
from PIL import Image
from utils import rgb_to_binary, add_leading_zeros

def main():
	img_visible_path = 'enc_3 (2).png';
	img_hidden_path = 'pngwing.com (9).png'
	output_path = 'encoded'
	filename, file_ext = os.path.splitext(output_path)
	output_path = filename + '.png'
	img_visible = Image.open(img_visible_path)
	img_hidden = Image.open(img_hidden_path)
	encoded_image = encode(img_visible, img_hidden)
	encoded_image.save(output_path)

def get_binary_pixel_values(img, width, height):
	hidden_image_pixels = ''
	for col in range(width):
		for row in range(height):
			pixel = img[col, row]
			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
			hidden_image_pixels += r_binary + g_binary + b_binary
	return hidden_image_pixels

def change_binary_values(img_visible, hidden_image_pixels, width_visible, height_visible, width_hidden, height_hidden):
	idx = 0
	for col in range(width_visible):
		for row in range(height_visible):
			if row == 0 and col == 0:
				width_hidden_binary = add_leading_zeros(bin(width_hidden)[2:], 12)
				height_hidden_binary = add_leading_zeros(bin(height_hidden)[2:], 12)
				w_h_binary = width_hidden_binary + height_hidden_binary
				img_visible[col, row] = (int(w_h_binary[0:8], 2), int(w_h_binary[8:16], 2), int(w_h_binary[16:24], 2))
				continue
			r, g, b = img_visible[col, row]
			r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
			r_binary = r_binary[0:4] + hidden_image_pixels[idx:idx+4]
			g_binary = g_binary[0:4] + hidden_image_pixels[idx+4:idx+8]
			b_binary = b_binary[0:4] + hidden_image_pixels[idx+8:idx+12]
			idx += 12
			img_visible[col, row] = (int(r_binary, 2), int(g_binary, 2), int(b_binary, 2))
			if idx >= len(hidden_image_pixels):
				return img_visible
	# can never be reached, but let's return the image anyway
	return img_visible

def encode(img_visible, img_hidden):
	encoded_image = img_visible.load()
	img_hidden_copy = img_hidden.load()
	width_visible, height_visible = img_visible.size
	width_hidden, height_hidden = img_hidden.size
	hidden_image_pixels = get_binary_pixel_values(img_hidden_copy, width_hidden, height_hidden)
	encoded_image = change_binary_values(encoded_image, hidden_image_pixels, width_visible, height_visible, width_hidden, height_hidden)
	return img_visible

if __name__ == '__main__':
	main()


