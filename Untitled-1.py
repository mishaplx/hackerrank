'''n = 17
x_n = []
x_oct = []
x_hex = []
x_bin = []
for i in range(1,n+1):
    x_oct.append(oct(i))
    x_hex.append(hex(i))
    x_bin.append(bin(i))

x_oct = ' '.join(''.join(x_oct).replace('0o',',').split(',')[1:])
x_hex = ' '.join(''.join(x_hex).replace('0x',',').split(',')[1:])
x_bin = ' '.join(''.join(x_bin).replace('0b',',').split(',')[1:])
for i in range(1, n+1):
    x_n.append(i)
    for i in range(len(x_n)):
        x_n[i] = str(x_n[i])
x_n = ','.join(x_n).replace(',',' ')
print(x_n)
print(x_oct)
print(x_hex)
print(x_bin)
'''
n = int(input())
w = len(str(bin(n)).replace('0b',''))

for i in range(1, n+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0o','', 1).rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print(j, o, h, b)