s = input("Enter the plain Text: ").upper()
k = input("Enter the key: ").upper()

s = s.replace(' ','')

def expand_Key(s, k):
    c = 0
    l = len(k)
    for i in range(len(s)-len(k)):
        k = k+k[c]
        if(c<len(k)):
            c += 1
        else:
            c = 0
    return k

def encrypt(s,k):
    ct = ""
    for i in range(len(s)):
        ascii = ((ord(s[i])+ord(k[i])-65)%26)+65
        ct += chr(ascii)
    return ct

def decrypt(ct,k):
    pt = ""
    for i in range(len(ct)):
        ascii = ((ord(ct[i])-ord(k[i])-65)%26)+65
        pt += chr(ascii)
    return pt
k = expand_Key(s,k)
ct = encrypt(s,k)
print(ct)
pt = decrypt(ct,k)
print(pt)
