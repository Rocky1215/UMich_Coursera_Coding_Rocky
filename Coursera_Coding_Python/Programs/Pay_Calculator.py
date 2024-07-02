hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hourly Rate:")
r = float(rate)

if h >= 40:
    ho = h - 40
    ro = r * 1.5
    po = ho * ro
    pn = 40 * r
    p = po + pn
    
else:
    p = h * r
print(p)