name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
entries = dict()
for line in fh:

    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        words = line.split(" ")
        word = words[1]
        entries[word] = entries.get(word, 0) + 1
        
commonemail = None
commoncount = None

for word, count in entries.items():
    if commoncount is None or count > commoncount:
        commonemail = word
        commoncount = count
print(commonemail, commoncount)
            
