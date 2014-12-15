rpyL for EBS Census
====
This program is used to generate graphs and analysis for the EBS census. Currently, given a list of names of csv files of data in the current directory, it can create all valid bar graphs for each csv file (assuming they have been cleaned before hand!)
###Compiling
I compiled it using py_compile.
###Running
```
python main2.py
```
or
```
python main2.pyc
```
You will be prompted for the list of csv files. They should be named by their grade. 11th grade's cs file is 11, for example. Support for total,ms,hs has not been added yet.
### Future Plans
-Box Plot support
-Attempting all correlation
-Data summary
-Mass hypothesis testing.
