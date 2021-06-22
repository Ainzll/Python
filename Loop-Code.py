# Loop-Code.py
# Encapsulation
print("DEC\tHEX\tBIN\tCHR")
for d in range(32,128):
	h = hex(d)
	h = h.replace("0x","$")
	b = bin(d)
	b = b.replace("0b"," - ")
	c = chr(d)
	#print(str(d)+" "+h,end="")
	print(str(d)+"\t"+h+"\t"+b+"\t"+c)

# str(d)+" " is a call concatination
# python3 "%f"
