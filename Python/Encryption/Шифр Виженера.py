act = int(input("Зашифровать - 0; расшифровывать - 1: "))
slovo = input("Введите слово: ")
zash = '0'
key = int(input("Ключ: "))
if act == 0:
    def encrypt_ceasar (slovo, zash):
        for c in range (len(slovo)):
            a = ord(slovo[c])
            a += key
            zash += str(chr(a))
        return zash
    print ('Зашифрованное слово: ' + str(encrypt_ceasar (slovo, zash)[1:]))
else:
    def decrypt_ceasar (slovo, zash):
        for c in range(len(slovo)):
            a = ord(slovo[c])
            a -= key
            zash += str(chr(a))
        return zash
    print ('Расшифрованное слово: ' + str(decrypt_ceasar (slovo, zash)[1:]))