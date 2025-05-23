fin = open("input.txt","a")
fin.writelines("\nWelcome to python programming.\nAi is the future.")
fin = open("input.txt","r")
fout= open("output.txt","w")

for line in fin:
    line = line.swapcase()
    line = line.replace(".","*")
    fout.write(line)

data = fin.read()
print(data)