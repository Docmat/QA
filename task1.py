file = open("air.txt","r")
symbols = {}

count = len(file)
a = set(file)
a.remove("\n")
a.remove ('.')
print(count)
print(a)
