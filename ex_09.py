name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
# finding from: lines
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
# splitting and stripping 2nd word
    line = line.split()
    email = line[1]
# creating a list for all addresses
    lst.append(email)
    emails = lst
# create dictionary (key is email address)
# use for loop to count
dict_email = dict()
for email in emails:
    dict_email[email] = dict_email.get(email,0) + 1
mostcommon = -1
mcemail = None
for k,v in dict_email.items():
    if v > mostcommon:
        mostcommon = v
        mcemail = k
    else: continue
# find most prolific sender
print(mcemail, mostcommon)