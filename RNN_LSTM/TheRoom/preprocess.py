#Source code with the blog post at http://monik.in/a-noobs-guide-to-implementing-rnn-lstm-using-tensorflow/
import numpy as np
import random
from random import shuffle

def file_len(fname):
    with open(fname, encoding="utf8") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

in_name = "data/seinfeld.txt"
out_name = "data/seinfeldProcessed.txt"
names_list_out = "data/seinfeldNames.txt"

print("counting lines in file...")
count=0
totalLen = 0
totalLen = file_len(in_name)

print("reading file...")
with open(in_name, encoding="utf8") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip('\n') for x in content] 

out = open(out_name, "w")

count = 0
prevCount = 0
for line in content:
    count += 1
    colon = line.find(":")
    if (colon > 0):
        name = line[:colon]
        upperName = name.upper()
        # print(upperName)
        out.write("\n")
        out.write(upperName);
        out.write("\n")
        body = line[colon+2:]
    else:
        body = line
    
    out.write(body)
    # print(body)
    if (len(body) > 0):
        out.write("\n")




#######################################################################################################