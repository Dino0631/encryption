prims = []
x = prims[0]
# print(key)
file = input("enter file to decrypt, with file extension( thing.txt not thing)")
file2 = input("enter file to decrypt to, with file extension( thing2.txt not thing2)")
with open(file, 'rb') as f:
	data = f.read()
e = b''
n = 0
for b in data:
	x = prims[n%(len(prims))]
	hexnum = hex((b*x)%256)[2:]
	hexnum = '0'*(2-len(hexnum))+hexnum
	print(hexnum)
	e += bytes(bytearray.fromhex(hexnum))
	n +=1

with open(file2, 'wb') as f:
	f.write(e)
input()