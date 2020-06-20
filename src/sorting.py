import random

def main():
    Sort = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    print("Before: " + str(Sort) + "\n")
    Memory = 999

    for i in range(-1,len(Sort)*10):
        for y in range(0,len(Sort)):
            if y+1 >= len(Sort):
                #print(str(Sort))
                quit
            else:
                if Sort[y] > Sort[y+1]:
                    Memory = Sort[y]
                    Sort[y] = Sort[y+1]
                    Sort[y+1] = Memory
    print("After: " + str(Sort))