import sys
try:
    file = open(sys.argv[1],"r")
    index = list(file.read().split(",")).index(sys.argv[2])
    print("Index:\t"+str(index)+"\n")
except Exception as e: 
    if type(e).__name__ == "ValueError":
        print("\n Not Found!\n")
    else:
        print(e)
        print("\n Usage: python3 <filename> <keyword>\n")
