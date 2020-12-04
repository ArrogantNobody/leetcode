d = {'a':1,'b':2,'c':3}
for i in range(3):
    d.setdefault('z', 0)+1

print(d)