import re
import time

t = time.time()

f = open('wordlist.txt', 'r')
for word in f:
    test = True
    start = word.find('a')
    if start != -1 and start < word.find('e') < word.find('i') < \
    word.find('o') < word.find('u') < word.find('y'):
        for v in 'aeiouy':
            if len(re.findall(v, word)) != 1:
                test = False
        if test: print word 
        test = True

print "finished in: %.2f sec" % float(time.time() - t)
                
        
