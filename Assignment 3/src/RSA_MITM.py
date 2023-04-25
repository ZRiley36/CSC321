

from Crypto.Util import number

def find_d(e, o):
    o = o + 1
    while True:
        if o % e == 0:
            return o // e
        o += o
        

def RSA():
    e = 65537
    num_length = 2048
    p = number.getPrime(num_length)
    q = number.getPrime(num_length)
    n = p*q
    o = (p-1)*(q-1)
    d = find_d(e, o)
    PU = (e, n)
    PR = (d, n)
    print (d)
    #encrypt
    message = "hello world"
    message =  int.from_bytes(message.encode(), byteorder='little')
    print(message)
    
    cipher_text = pow(message, e, n)
   
    plain_text = pow(cipher_text, d, n)
    
    print(plain_text)




if __name__ == "__main__":
    RSA()
    