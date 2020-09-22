

stringlist = []
Memory = ""

def main():
	f = open("stringlist.txt", "w+")
	for i in f:
		stringlist.append(i)

	f.close()

	print(stringlist)

	for i in range(-1,len(stringlist)*100):
		for y in range(0, len(stringlist)):
			if y+1 >= len(stringlist):
				quit
			else:
				if len(stringlist[y]) > len(stringlist[y+1]):
					Memory = stringlist[y]
					stringlist[y] = stringlist[y+1]
					stringlist[y+1] = Memory
	
	f = open("sorted.txt", "w")

	for i in range(0, len(stringlist)):
		f.write(i)
		print(i)

	f.close()