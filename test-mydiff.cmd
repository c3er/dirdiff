@echo off

:START

rem echo %~dp0

python mydiff.py -u                                                 dir1.txt dir2.txt
python mydiff.py -n                                                 dir1.txt dir2.txt
python mydiff.py -c                                                 dir1.txt dir2.txt
python mydiff.py                                                    dir1.txt dir2.txt
python mydiff.py    -l 1                                            dir1.txt dir2.txt
                                                                   
python mydiff.py -u      -o test\dirdiff1.txt                       dir1.txt dir2.txt
python mydiff.py -n      -o test\dirdiff2.txt                       dir1.txt dir2.txt
python mydiff.py -c      -o test\dirdiff3.txt                       dir1.txt dir2.txt
python mydiff.py         -o test\dirdiff4.txt                       dir1.txt dir2.txt
python mydiff.py    -l 1 -o test\dirdiff5.txt                       dir1.txt dir2.txt

python mydiff.py                             -m test\dirdiff1.html  dir1.txt dir2.txt
python mydiff.py    -l 1                     -m test\dirdiff2.html  dir1.txt dir2.txt
python mydiff.py -c -l 1                     -m test\dirdiff3.html  dir1.txt dir2.txt

:: Error cases
python mydiff.py         -o dirdiff.txt -m dirdiff.html             dir1.txt dir2.txt
python mydiff.py                                                    dir1.txt
python mydiff.py                                                             dir2.txt
python mydiff.py                                                    foo.txt  bar.txt

pause
goto START