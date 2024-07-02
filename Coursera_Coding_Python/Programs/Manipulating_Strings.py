text = "X-DSPAM-Confidence:    0.8475"
spos = text.find('0')
epos = text.find('5') + 1
snum = text[23:29]
fnum = float(snum)
print(fnum)