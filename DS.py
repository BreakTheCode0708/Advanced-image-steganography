from PIL import Image
def euclid(m, n):

	if n == 0:
		return m
	else:
		r = m % n
		return euclid(n, r)

# Multiplicative inverse
def exteuclid(a, b):

	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)

	while r2 > 0:

		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t

	if t1 < 0:
		t1 = t1 % a

	return (r1, t1)

# Enter two large prime
# numbers p and q
p = 823
q = 953
n = p * q
Pn = (p-1)*(q-1)

# Generate encryption key
# in range 1<e<Pn
key = []

for i in range(2, Pn):

	gcd = euclid(Pn, i)

	if gcd == 1:
		key.append(i)

# Select an encryption key from list
e = int(313)

# Obtain inverse of encryption key in Z_Pn
r, d = exteuclid(Pn, e)
if r == 1:
	d = int(d)
	print("decryption key is: ", d)
else:
	print("Multiplicative inverse for\ the given encryption key does not \exist. Choose a different encryption key ")

def rsakeys():
	privatekey = d
	publickey = e
	return privatekey, publickey

def sign(privatekey,data):
	S = (data ** privatekey) % n
	return S

def verify(data,sign,publickey):
	M1 = (sign ** publickey) % n
	if data == M1:
		return True
	else:
		return False
