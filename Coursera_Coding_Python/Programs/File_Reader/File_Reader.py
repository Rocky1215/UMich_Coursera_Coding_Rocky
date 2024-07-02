# Use words.txt as the file name (Path Name)
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File not found: ' + fname)
    quit()

for line in fh:
    line = line.rstrip().upper()
    print(line)