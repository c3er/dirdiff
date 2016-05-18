@echo off

:START

rem echo %~dp0

python mydiff.py         -m dirdiff.html                 dir1.txt dir2.txt
python mydiff.py    -l 1 -m dirdiff.html                 dir1.txt dir2.txt
python mydiff.py -c -l 1 -m dirdiff.html                 dir1.txt dir2.txt
python mydiff.py -u                                      dir1.txt dir2.txt
python mydiff.py -n                                      dir1.txt dir2.txt
python mydiff.py -c                                      dir1.txt dir2.txt
python mydiff.py                                         dir1.txt dir2.txt
python mydiff.py    -l 1                                 dir1.txt dir2.txt

python mydiff.py -u                      -o dirdiff.txt  dir1.txt dir2.txt
python mydiff.py -n                      -o dirdiff.txt  dir1.txt dir2.txt
python mydiff.py -c                      -o dirdiff.txt  dir1.txt dir2.txt
python mydiff.py                         -o dirdiff.txt  dir1.txt dir2.txt
python mydiff.py    -l 1                 -o dirdiff.txt  dir1.txt dir2.txt

python mydiff.py         -m dirdiff.html -o dirdiff.txt  dir1.txt dir2.txt
python mydiff.py    -l 1 -m dirdiff.html -o dirdiff.txt  dir1.txt dir2.txt
python mydiff.py -c -l 1 -m dirdiff.html -o dirdiff.txt  dir1.txt dir2.txt

pause
goto START