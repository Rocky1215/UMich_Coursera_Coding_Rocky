# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tnum = None
cnum = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        
    snum = line.find('0')
    num = line[snum:]
    fnum = float(num)
    if tnum is None:
        tnum = fnum
    else:
        tnum = tnum + fnum
    
    if cnum is None:
        cnum = 1
    else:
        cnum = cnum + 1

anum = tnum / cnum    
print('Average spam confidence:' , anum)