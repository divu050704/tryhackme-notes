#!/bin/bash/python3
import csv
# Open the dumped file, you find this in the output while dumping
file = open("/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm/dump/blog/users.csv", 'r')
data = csv.reader(file)
passwords = []
for i in data:
    # Last row was f*****ng empty
    if len(i) == 3:
        passwords.append(i[1]+"\n")
file.close()
file = open("dict","w")
file.writelines(passwords)
file.close()
