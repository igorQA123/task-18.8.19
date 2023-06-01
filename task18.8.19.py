n = int(input('Skolko biletov vy hotite priobresti?'))
s = 0
i = 1
for i in range(1, n +1):
    adg = int(input('Vozrast posetitelja?'))
    if 18 <= adg < 25:
        s = s + 990
    if adg >= 25:
        s = s + 1390
if n > 3:
    s *= 0.9
print('Summa k oplate', s)