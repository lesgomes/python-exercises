name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
number = list()
d = dict()
count = 0
for line in handle:
    line.rstrip()
    if line.startswith('From '):
        time = line.split()
        hours.append(time[5])
for hour in hours:
    number.append(hour[:2])
for c in number:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
for k,v in sorted(d.items()):
    print(k,v)