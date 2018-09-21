from pathlib import Path

my_file = Path("./testdir/test3.txt")
if my_file.is_file() == True:
    print("Test 1 Passed")
else:
    print("Test Failed 1")

my_file = Path("./testdir/test4.txt")
if my_file.is_file() == False:
    print("Test 2 Passed")
else:
    print("Test Failed 2")
