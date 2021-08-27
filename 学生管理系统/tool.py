import hashlib
def encrypt_password(password,x='wmm'):
    h=hashlib.sha256()
    h.update(password.encode('utf-8'))
    h.update(x.encode('utf-8'))
    print(h.hexdigest())
    return h.hexdigest()
if __name__ == '__main__':
    encrypt_password('123456')