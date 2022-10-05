import requests
import sys
string = "${{<%[%'\"}}%"

for i in range(len(string)):
    for j in (i,len(string)):
        #requests.get("http://10.10.55.183:5000/profile"+)
        for k in range(j,len(string)):
            req = requests.get(sys.argv[1]+str(string[i:k]))
            if (req.status_code) == 500:
              print("This is breaking the system:\t"+"http://10.10.55.183:5000/profile/"+str(string[i:k]))
#req = requests.get("http://10.10.55.183:5000/profile/{{")
#print(req.status_code)
