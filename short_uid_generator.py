import uuid

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8","9"]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def generate_short_uid():
	uid = ""
	long_id = str(uuid.uuid4())
	long_id = long_id.replace("-","")
	#print("long: " + long_id)
	for i in range(8):
		s = long_id[i*4:i*4+4]
		x = int(s,16)
		if i == 0:
			uid += alphabet[x % 0x1a]	
		else:
			uid += chars[x % 0x24]
	#print("short: " + uid)
	return uid

if __name__ == "__main__":
	d = {}
	print(generate_short_uid())
	for i in range(1000000):
		uid = generate_short_uid()
		if uid in d:
			print("第"+str(i)+"次发现冲突")
			print(uid)
			exit()
		d[uid] = 1
	print("100万次生成无冲突")	
