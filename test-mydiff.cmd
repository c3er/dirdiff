@echo off

:START

rem echo %~dp0

python mydiff.py dir1.txt dir2.txt
python mydiff.py dir1.txt dir2.txt -c
python mydiff.py dir1.txt dir2.txt -u
python mydiff.py dir1.txt dir2.txt -n
python mydiff.py dir1.txt dir2.txt    -l 1

python mydiff.py dir1.txt dir2.txt         -o test\dirdiff4.txt
python mydiff.py dir1.txt dir2.txt -c      -o test\dirdiff3.txt
python mydiff.py dir1.txt dir2.txt -u      -o test\dirdiff1.txt
python mydiff.py dir1.txt dir2.txt -n      -o test\dirdiff2.txt
python mydiff.py dir1.txt dir2.txt    -l 1 -o test\dirdiff5.txt

python mydiff.py dir1.txt dir2.txt         -o test\dirdiff1.html
python mydiff.py dir1.txt dir2.txt    -l 1 -o test\dirdiff2.html
python mydiff.py dir1.txt dir2.txt -c -l 1 -o test\dirdiff3.html

:: Error cases
python mydiff.py
python mydiff.py dir1.txt dir2.txt         -m test\dirdiff.html
python mydiff.py dir1.txt
python mydiff.py          dir2.txt
python mydiff.py foo.txt  bar.txt

:: Print usage
python mydiff.py -h
python mydiff.py    --help

pause
goto START