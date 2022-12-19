s = input("Enter the plain Text: ").upper()
k = int(input("Enter the key: "))


def encrypt(PT, key):
    ct = ""
    for i in PT:
        if(i != ' '):
            ascii = ((ord(i)+key-65) % 26)+65
            ct += chr(ascii)
        else:
            ct += i
    return ct

def decrypt(ct,key):
    pt = ""
    for i in ct:
        if(i != ' '):
            ascii = ((ord(i)-key-65) % 26)+65
            pt += chr(ascii)
        else:
            pt += i
    return pt



ct = encrypt(s, k)
print(decrypt(ct,k))
