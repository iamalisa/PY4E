fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

for i in fh:
    i = i.rstrip()
    if i.startswith('From '):
        count = count + 1
        j = i.split()
        print(j[1])

print("There were", count, "lines in the file with From as the first word")
