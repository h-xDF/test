from simplecrypt import *
# класс с созданными классами исключений , тоже необхоимо импортировать

pas_list = []

with open("Password.txt","rb") as inp:
    for line in inp:
        pas_list.append(line.strip())


    # pas_list.append(pas)
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    for pas in pas_list:
        try:
            var = decrypt(pas,encrypted).decode('utf8')
        except DecryptionException:
            pass
    try:
        print(var)
    except NameErorr:
        print('Неудалось расшифровать')
