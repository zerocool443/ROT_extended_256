def decrypt(ciphertext):
    """Decrypt the string and return the plaintext"""
    for i in range(256):
        
        result = ''
        for l in ciphertext:
            try:
                    a = chr((ord(l) + i)% 256)
                    result = result +str(a);
            except:
                print('exception')
        print(result)

message = input('Enter the cipher text')

decrypt(str(message))

