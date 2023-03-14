import random
file=open("nothing.txt","w")
file.write("line 1 \n line 2 \n line 3 \n line 4 \n line 5")
file.close()

def randomLine(file_name):
    lines=open(file_name).read().splitlines()
    return random.choice(lines)
print(randomLine('nothing.txt'))
