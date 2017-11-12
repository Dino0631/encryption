prims = []
file = input("enter file to encrypt, with file extension( thing.txt not thing)").strip()
file2 = input("enter file to encrypt to, with file extension( thing2.txt not thing2)").strip()
with open(file, 'rb') as f:
	data = f.read()
n=0
decdata = b''
for b in data:
	x = prims[n%(len(prims))]

	c = 0
	while c<256 and x*c%256!=b:
		c+=1
	hexnum = hex(c)[2:]
	hexnum = '0'*(2-len(hexnum))+hexnum
	decdata += bytes(bytearray.fromhex(hexnum))
	print(chr(c))
	n+=1
with open(file2, 'wb') as f:
	f.write(decdata)