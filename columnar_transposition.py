import math


def encrypt(key, plain_text):
    key_list = [*key]
    sort_keyList = sorted(key_list)
    plain_text_List = [*plain_text]
    arr = []
    j = 1
    for i in sort_keyList:
        arr.append(j)
        j = j + 1
    a = []
    count = 0
    dictionary = {}
    for i in range(len(arr)):
        dictionary[str(arr[i])] = sort_keyList[i]
    for i in range(int(len(plain_text)/len(key))+1):
        b = []
        for j in range(len(arr)):
            if(count < len(plain_text)):
                b.append(plain_text_List[count])
                count = count+1
            else:
                b.append('X')
        a.append(b)
    s = ""
    B = [*zip(*a)]
    for i in range(len(arr)):
        index = key_list.index(dictionary[str(arr[i])])
        key_list[index] = ' '
        b = B[index]
        for j in range(0, len(a)):
            s += b[j]

    return s


def decrypt(key, CT):
    key_list = [*key]
    sort_keyList = sorted(key_list)
    CT_List = [*CT]
    arr = []
    j = 1
    for i in sort_keyList:
        arr.append(j)
        j = j + 1
    a = []
    count = 0
    dictionary = {}
    for i in range(len(arr)):
        dictionary[str(arr[i])] = sort_keyList[i]
    for i in range(len(arr)):
        b = []
        for j in range(int(len(plain_text)/len(key))+1):
            if(count < len(CT)):
                b.append(CT_List[count])
                count = count+1
        a.append(b)
    s = ""
    ans = [[] for _ in range(int(len(plain_text)/len(key))+1)]
    for j in range(int(len(plain_text)/len(key))+1):
        l = sort_keyList.copy()
        for i in range(len(key_list)):
            column = l.index(key_list[i])
            l[column] = ''
            an = a[column]
            ans[j].append(an[j])
    for i in range(len(ans)):
        an = ans[i]
        for j in an:
            s += j

    return s


key = input('Enter the key: ')
plain_text = input('Enter the plain text: ')
s = encrypt(key, plain_text)
print('Encrypted text: '+s)
s = decrypt(key, s)
print('Decrypted text: '+s)
