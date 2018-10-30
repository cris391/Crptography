import hashlib

# m = hashlib.sha1(b"1d60+m").hexdigest()
# m = hashlib.sha1(b"1d60+m").hexdigest()
m = hashlib.sha1(b"m").hexdigest()
M = hashlib.sha1(b"M").hexdigest()

import itertools

stuff = ['m', 'M', '1', '!', '6', '&', '0', '=','?','+', 'd', 'D']
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        str1 = ''.join(subset)
        # print(hashlib.sha1(b"{str1}").hexdigest())
        print("{str1}")
        if(hashlib.sha1(b"str1").hexdigest()=='29325ad40aa35e83fb2066d10c7c75122c082205'):
          print()