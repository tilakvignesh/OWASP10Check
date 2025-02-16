# hash crack script for md5

import argparse
import hashlib

def hashcracker(hash, wordlist):
    try:
        file = open(wordlist, 'r')
        cracked_val = None
        for raw in file:
            word = raw.strip()
            word_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
            if word_hash.lower() == hash or word_hash.upper() == hash:
                cracked_val = word
                break
        return cracked_val
    except Exception as e:
        raise e

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take the hash val and wordlist')
    parser.add_argument('-w', '--wordlist', help = 'path to your Wordlist', required = True)
    parser.add_argument('-x', '--hashedVal', help = 'md5 hash', required = True)
    args = parser.parse_args()
    hash = args.hashedVal
    wordlist = args.wordlist

    ans = hashcracker(hash, wordlist)
    if ans == None:
        print('Hash Not Found, try using a more extensive wordlist')
    else:
        print('The Word was', ans)