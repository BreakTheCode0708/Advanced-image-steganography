def add_leading_zeros(binary_number, expected_length):
	length = len(binary_number)
	return (expected_length - length) * '0' + binary_number

def rgb_to_binary(r, g, b):
	return add_leading_zeros(bin(r)[2:], 8), add_leading_zeros(bin(g)[2:], 8), add_leading_zeros(bin(b)[2:], 8)