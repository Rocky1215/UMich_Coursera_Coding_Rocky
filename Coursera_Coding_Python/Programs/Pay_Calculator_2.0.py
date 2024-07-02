hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

def computepay(h, r):
    if h > 40:
        ho = h - 40
        ro = r * 1.5
        po = ho * ro
        pn = 40 * r
        return pn + po
        
    else:
        return h * r

p = computepay(h , r)
print("Pay", p)