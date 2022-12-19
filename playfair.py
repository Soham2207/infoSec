s = input("Enter the plain Text: ").upper()
k = input("Enter the key: ").upper()

a = [[] for _ in range(5)]
l = [i for i in range(65,91)]
s = s.replace(' ','X')
print(l)
j = 0
for i in k:
    if(len(a[j])<5):
        if(l.__contains__(ord(i))):
            a[j].append(i)
            l.remove(ord(i))
    else:
        j = j+1
        if(l.__contains__(ord(i))):
            a[j].append(i)
            l.remove(ord(i))

for i in l:
    if l.__contains__(73) and l.__contains__(74) and i == 73:
        if(len(a[j])<5):
            a[j].append(chr(i))
            
        else:
            j += 1
            a[j].append(chr(i))
            
    elif l.__contains__(73) and l.__contains__(74) and i == 74:
        a[j][len(a[j])-1] += '/J'
        continue
    elif (l.__contains__(73) == False or l.__contains__(74) == False) and i == 89:
        if(len(a[j])<5):
            a[j].append(chr(i))
            
        else:
            j += 1
            a[j].append(chr(i))
            
    elif (l.__contains__(73) == False or l.__contains__(74) == False) and i == 90:
        a[j][len(a[j])-1] += '/Z'
        continue
    elif(len(a[j])<5):
        a[j].append(chr(i))
        
    else:
        j += 1
        a[j].append(chr(i))
        

def find(c):
    if(c== 'I' or c == 'J'):
        c = 'I/J'
    for i in range(5):
        b = a[i]
        for j in range(5):
            if(b[j] == c):
                return i,j
i = 0
k = len(s)
while(s[i] != s[k-1]):
    if s[i] == s[i-1] and i !=0:
        s = s[:i] + 'X' + s[i:]
        k = k+1
    i += 1

if(len(s)%2 != 0):
    s += 'X'

def encrypt(s):
    c = 0
    e = ""
    for i in range(int(len(s)/2)):
        b = s[c:c+2]
        r1,c1 = find(b[0])
        r2,c2 = find(b[1])
        l1 = a[r1]
        l2 = a[r2]
        if(r1 == r2):
            if(c1 == 4):
                e += l1[0]
            else:
                e += l1[c1+1]
            if(c2 == 4):
                e += l2[0]
            else:
                e += l2[c2+1]
        elif(c1 == c2):
            if(r1 == 4):
                l1 = a[0]
            else:
                l1 = a[r1+1]
            if(r2 == 4):
                l2 = a[0]
            else:
                l2 = a[r2+1]
            e += l1[c1]
            e += l2[c2]
        else:
            e += l1[c2]
            e += l2[c1]
        c = c+2
    return e


def decrypt(s):
    c = 0
    e = ""
    for i in range(int(len(s)/2)):
        b = s[c:c+2]
        r1,c1 = find(b[0])
        r2,c2 = find(b[1])
        l1 = a[r1]
        l2 = a[r2]
        if(r1 == r2):
            if(c1 == 0):
                e += l1[4]
            else:
                e += l1[c1-1]
            if(c2 == 0):
                e += l2[4]
            else:
                e += l2[c2-1]
        elif(c1 == c2):
            if(r1 == 0):
                l1 = a[4]
            else:
                l1 = a[r1-1]
            if(r2 == 0):
                l2 = a[4]
            else:
                l2 = a[r2-1]
            e += l1[c1]
            e += l2[c2]
        else:
            e += l1[c2]
            e += l2[c1]
        c = c+2
    return e    

ct = encrypt(s)
print(decrypt(ct))