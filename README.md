# replace-in-specified-column
You can replace the specific value in specified column of the CSV file with the value you specify. You set [filename], [column number], [value before change], [value after change] and run this software on Terminal, then this software makes new CSV file(YYYYMMDDHHM24Ss.csv).

# Dependency
Python3

# Setup
You must only have any Python environment. You can use this software at Terminal.

# Usage
`python replace.py file.csv 1 apple banana`  

file.csv before change  
 >id,fruit,price  
 >100,**apple**,100  
 >200,water melon,200  
 >300,grape,300  

new csv after change  
 >id,fruit,price  
 >100,**banana**,100  
 >200,water melon,200  
 >300,grape,300  

`python replace.py file.csv 2 200 400`  

file.csv before change  
 >id,fruit,price  
 >100,apple,100  
 >**200**,water melon,**200**  
 >300,grape,300  

new csv after change  
 >id,apple,price  
 >100,banana,100  
 >**200**,water melon,**400**  
 >300,grape,300  
