This is just various scripts repo

Example commit:

drwxrwxrwx 1 XXXXXX XXXXXX 4096 Aug 27 21:22 ..
-rw-rw-rw- 1 XXXXXX XXXXXX 1441 Aug 27 21:25 gcal.py
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ vim gcal.py
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ cp ~/notes.txt notes.txt
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ vim notes.txt
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ git add gcal.py
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ git add notes.txt
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ git commit -m "Add initial file (gcal.py) with notes file"
[master e25705e] Add initial file (gcal.py) with notes file
 2 files changed, 45 insertions(+)
 create mode 100644 church_cal/gcal.py
 create mode 100644 church_cal/notes.txt
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$ git push origin master
Username for 'https://github.com': XXXXXXXXXXXXXXX
Password for 'https://jcukuleleband@github.com':  XXXXXXXXXXXX
Counting objects: 5, done.
Delta compression using up to 12 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.32 KiB | 674.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To https://github.com/jcukuleleband/scripts.git
   0fb37ab..e25705e  master -> master
XXXXXXXXXXXXXXXXXXXX:~/github/scripts/church_cal$
