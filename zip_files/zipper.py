from zipfile import ZipFile

files = []
files.append("./test1.txt")
files.append("./testdir/test2.txt")
files.append("./testdir/test3.txt")

# writing files to a zipfile
with ZipFile('my_python_files.zip','w') as zip:
# writing each file one by one
  for file in files:
    zip.write(file)

zip.close()
