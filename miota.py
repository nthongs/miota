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


# Test function
if __name__ == '__main__':
    seed = generate_seed()
    print(seed)
