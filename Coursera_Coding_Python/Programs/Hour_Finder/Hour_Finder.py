name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
entries = dict()

for line in handle:
    if line.startswith("From:"):
        continue
        
    elif line.startswith("From"):
        words = line.split()
        word = words[5]
        word = word.split(":")
        number = word[0]
        entries[number] = entries.get(number, 0) + 1
        
for (k,v) in sorted(entries.items()):
    print(k,v)