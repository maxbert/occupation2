max.bertfield@cslab1-24:~$ cd doft-dev/MaxandWill
max.bertfield@cslab1-24:~/doft-dev/MaxandWill$ . ../ve/bin/activate
(ve)max.bertfield@cslab1-24:~/doft-dev/MaxandWill$ python occu.py
python: can't open file 'occu.py': [Errno 2] No such file or directory
(ve)max.bertfield@cslab1-24:~/doft-dev/MaxandWill$ ls
#occupation.py#  occupation.py
(ve)max.bertfield@cslab1-24:~/doft-dev/MaxandWill$ cd ..
(ve)max.bertfield@cslab1-24:~/doft-dev$ cd occupation2/
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ python occu.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 251-916-264
127.0.0.1 - - [27/Sep/2016 14:20:07] "GET /occupations HTTP/1.1" 301 -
127.0.0.1 - - [27/Sep/2016 14:20:09] "GET /occupations/ HTTP/1.1" 200 -
127.0.0.1 - - [27/Sep/2016 14:20:09] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [27/Sep/2016 14:20:09] "GET /favicon.ico HTTP/1.1" 404 -
  C-c C-c(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ deactivate
max.bertfield@cslab1-24:~/doft-dev/occupation2$ git commit -am "fixed route"
[master 3ef08a4] fixed route
 1 file changed, 1 insertion(+), 1 deletion(-)
max.bertfield@cslab1-24:~/doft-dev/occupation2$ git push
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 293 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.        
To git@github.com:maxbert/occupation2.git
   6ec061a..3ef08a4  master -> master
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls
occupations.csv  occu.py  occu.py~  README.md  templates
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mkdir utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv occu.py utitls/occupation.py
mv: cannot move ‘occu.py’ to ‘utitls/occupation.py’: No such file or directory
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv occu.py utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$mkdir data
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv occupations.csv data
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls
data  occu.py  occu.py~  README.md  templates  utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls utils
occu.py
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls daata
ls: cannot access daata: No such file or directory
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls data
occupations.csv
max.bertfield@cslab1-24:~/doft-dev/occupation2$ rm occu.py
max.bertfield@cslab1-24:~/doft-dev/occupation2$ rm.occu.py~
rm.occu.py~: command not found
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls
data  occu.py~  README.md  templates  utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$ rm *~
max.bertfield@cslab1-24:~/doft-dev/occupation2$ . ../ve/bin/activate
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ deactivate
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv ../occu.py /
mv: cannot stat ‘../occu.py’: No such file or directory
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv utils/occu.py /
mv: cannot create regular file ‘/occu.py’: Permission denied
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv utils/occu.py occupation2/
mv: cannot move ‘utils/occu.py’ to ‘occupation2/’: Not a directory
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv utils/occu.py ..
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls
data  README.md  templates  utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls ..
flask_app_example  ShamaulSarahMaxDilmohamedYoonBertfield  templates
MaxandWill         template1.py                            test.html
occupation2        template1.py~                           test.html~
occu.py            #template.py#                           ve
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv occu.py occupations2
mv: cannot stat ‘occu.py’: No such file or directory
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv ../occu.py occupations2
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls
data  occupations2  README.md  templates  utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv occupations2 occu.py
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls
data  occu.py  README.md  templates  utils
max.bertfield@cslab1-24:~/doft-dev/occupation2$ mv ../MaxandWill/occupation.py utils/occu.py
max.bertfield@cslab1-24:~/doft-dev/occupation2$ ls utils
occu.py
max.bertfield@cslab1-24:~/doft-dev/occupation2$ . ../ve/bin/activate
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ python occu.py
Traceback (most recent call last):
  File "occu.py", line 3, in <module>
    from utils import occupation
ImportError: No module named utils
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ cd utils
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2/utils$ touch __init__.py
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2/utils$ cd ..
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ python occu.py
Traceback (most recent call last):
  File "occu.py", line 3, in <module>
    from utils import occupation
ImportError: cannot import name occupation
(ve)max.bertfield@cslab1-24:~/doft-dev/occupation2$ 