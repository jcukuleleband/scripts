filename = "test.txt"
file = open (filename, "r")
for line in file:
  l = line.strip()
  if l.startswith("#")==False:
    print(l)
file.close()
