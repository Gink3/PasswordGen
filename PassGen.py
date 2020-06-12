#!/usr/bin/env python3

import random

# Change this to increase number of words in the password
wordCount = 3

# Change this for the correct file
filename = "corncob_lowercase.txt"

with open(filename) as f:
    passwd = ""
    content = f.readlines()
    content = [x.strip() for x in content]
    
    # Select words from word list
    for i in range(wordCount):
        passwd += content[random.randint(1,len(content))].title()

    passwd += str(random.randint(100,999))
    print(passwd)