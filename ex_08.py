fname = input("Enter file name: ")
fh = open(fname)
lst = list()
wordlist = list()
for line in fh:
    words = line.split()
    lst.append(words)
lst = lst[0] + lst[1] + lst[2] + lst[3]
lst.sort()
for w in lst:
    if w in wordlist:
        continue
    else:
        wordlist.append(w)
print(wordlist)

##############

fname = "mbox-short.txt"

fh = open(fname)
count = 0

for lines in fh:
    lines = lines.rstrip()
    if not lines.startswith('From ') : continue
    count = count + 1
    words = lines.split()
    email = words[1]
    print(email)

print("There were", count, "lines in the file with From as the first word")
