# Edgar Allen Poe's Address

### Difficulty: advanced 

### Type: programming

### Hint: There's an address that E.A. Poe would have found strange... Find and remove it from his book! E.A. wants to Make Darn 5ure his book is the same as the original... How can he Make Darn 5ure?

### Flag: ef192f313be2a2e21e6bdf03e98f8a02

### Solution:

    ~$ grep -o -rnw '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' The-Works-of-Edgar-Allen-Poe-Vol-2.txt

    #line 6735: 127.0.0.1

    # remove the ip address and use this command to get the md5sum:
    ~$ m5dsum The-Works-of-Edgar-Allen-Poe-Vol-2.txt
    
    #ef192f313be2a2e21e6bdf03e98f8a02  The-Works-of-Edgar-Allen-Poe-Vol-2.txt
    #The hash  output is the flag: ef192f313be2a2e21e6bdf03e98f8a02
