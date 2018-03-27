# Author: Nguyen Ti Hon, email: nthon01@gmail.com
# Working in Can Tho University
# I would like to define some small but useful function to support IOTA
# I try to make it to be compatible with python 2 and python 3
# Feel free to used it in your own code
# I this script I use PyOTA: https://github.com/iotaledger/iota.lib.py


def generate_seed():
    from random import SystemRandom
    alpha9 = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = 81
    generator = SystemRandom()
    return u''.join(generator.choice(alpha9) for _ in range(length))


def encrypt_seed(seed, password):
    # Remember that you must keep the return KEY to decrypt your ENCRYPTED SEED
    import base64
    import os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    salt = os.urandom(1024)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1000000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)
    f = Fernet(key)
    # The output are encrypted seed and key
    return [f.encrypt(seed), key]


def decrypt_seed(encrypted_seed, key):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return f.decrypt(encrypted_seed)


def get_balance(seed, node):
    from iota import Iota
    api = Iota(node, seed)
    acc_data = api.get_account_data()
    return acc_data['balance']



# Test function
if __name__ == '__main__':
    seed = generate_seed()
    print(seed)
