'''
'''
'''
File Handling

As the part of programming requirement, we have to store our data permanently for
future purpose. For this requirement we should go for files.
Files are very common permanent storage areas to store our data.

Types of Files:
=================
There are 2 types of files

1. Text Files:
==============
Usually we can use text files to store character data
eg: abc.txt

2. Binary Files:
===============
Usually we can use binary files to store binary data like images,video files, audio files etc...

Opening a File:

Before performing any operation (like read or write) on the file,first we have to open that
file.For this we should use Python's inbuilt function open()

But at the time of open, we have to specify mode,which represents the purpose of
opening file.

f = open(filename, mode)

The allowed modes in Python are

1. r  open an existing file for read operation. The file pointer is positioned at the
beginning of the file.If the specified file does not exist then we will get
FileNotFoundError.This is default mode.

2. w  open an existing file for write operation. If the file already contains some data
then it will be overridden. If the specified file is not already avaialble then this mode will
create that file.

3. a  open an existing file for append operation. It won't override existing data.If the
specified file is not already avaialble then this mode will create a new file.

4. r+  To read and write data into the file. The previous data in the file will not be
deleted.The file pointer is placed at the beginning of the file.

5. w+  To write and read data. It will override existing data.

6. a+  To append and read data from the file.It wont override existing data.

7. x  To open a file in exclusive creation mode for write operation. If the file already
exists then we will get FileExistsError.

Note: All the above modes are applicable for text files. If the above modes suffixed with
'b' then these represents for binary files.

Eg: rb,wb,ab,r+b,w+b,a+b,xb
f = open("abc.txt","w")
We are opening abc.txt file for writing data.

Closing a File:
After completing our operations on the file,it is highly recommended to close the file.
For this we have to use close() function.
f.close()

Various properties of File Object:

Once we opend a file and we got file object,we can get various details related to that file
by using its properties.

name  Name of opened file
mode  Mode in which the file is opened
closed  Returns boolean value indicates that file is closed or not
readable() Retruns boolean value indicates that whether file is readable or not
writable() Returns boolean value indicates that whether file is writable or not.



f=open('emp.txt','w')
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
print(f.fileno())

Writing data to text files:

We can write character data to the text files by using the following 2 methods.

write(str)
writelines(list of lines)

f=open('emp.txt','w')
f.write('Dhananjay')
f.write('good boy\n')
f.close()

Note: In the above program, data present in the file will be overridden everytime if we
run the program. Instead of overriding if we want append operation then we should open
the file as follows.

f = open("abcd.txt","a")

1) f=open("abcd.txt",'w')
2) list=["sunny\n","bunny\n","vinny\n","chinny"]
3) f.writelines(list)
4) print("List of lines written to the file successfully")
5) f.close()

Note: while writing data by using write() methods, compulsory we have to provide line
seperator(\n),otherwise total data should be written to a single line.

Reading Character Data from text files:
======================================

We can read character data from text file by using the following read methods.

read() To read total data from the file
read(n)  To read 'n' characters from the file
readline() To read only one line
readlines() To read all lines into a list

To read total data from the file
1) f=open("abc.txt",'r')
2) data=f.read()
3) print(data)
4) f.close()

To read only first 10 characters:
1) f=open("abc.txt",'r')
2) data=f.read(10)
3) print(data)
4) f.close()

To read data line by line:
1) f=open("abc.txt",'r')
2) line1=f.readline()
3) print(line1,end='')
4) line2=f.readline()
5) print(line2,end='')
6) line3=f.readline()
7) print(line3,end='')
8) f.close()


To read all lines into list:
1) f=open("abc.txt",'r')
2) lines=f.readlines()
3) for line in lines:
4) print(line,end='')
5) f.close()


f=open("abc.txt","r")
2) print(f.read(3))
3) print(f.readline())
4) print(f.read(4))
5) print("Remaining data")
6) print(f.read())


The with statement:

The with statement can be used while opening a file.We can use this to group file
operation statements within a block.
The advantage of with statement is it will take care closing of file,after completing all
operations automatically even in the case of exceptions also, and we are not required to
close explicitly.

Eg:
1) with open("abc.txt","w") as f:
2) f.write("Durga\n")
3) f.write("Software\n")
4) f.write("Solutions\n")
5) print("Is File Closed: ",f.closed)
6) print("Is File Closed: ",f.closed)
7)
8) Output
9) Is File Closed: False
10) Is File Closed: True


tell():
==>We can use tell() method to return current position of the cursor(file pointer) from
beginning of the file. [ can you plese telll current cursor position]
The position(index) of first character in files is zero just like string index.
Eg:
1) f=open("abc.txt","r")
2) print(f.tell())
3) print(f.read(2))
4) print(f.tell())
5) print(f.read(3))
6) print(f.tell())
abc.txt:
sunny
bunny
chinny
vinny


f=open("abc.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())


seek():
=======

We can use seek() method to move cursor(file pointer) to specified location.
[Can you please seek the cursor to a particular location]

f.seek(offset, fromwhere)

offset represents the number of positions

The allowed values for second attribute(from where) are

0---->From beginning of file(default value)
1---->From current position
2--->From end of the file

Note: Python 2 supports all 3 values but Python 3 supports only zero.

Note:
sys.exit(0) ===>To exit system without executing rest of the program.
argument represents status code . 0 means normal termination and it is the default value.

Handling Binary Data:
It is very common requirement to read or write binary data like images,video files,audio
files etc.
Q. Program to read image file and write to a new image file?
1) f1=open("rossum.jpg","rb")
2) f2=open("newpic.jpg","wb")
3) bytes=f1.read()
4) f2.write(bytes)
5) print("New Image is available with the name: newpic.jpg")

Handling csv files:
CSV==>Comma seperated values
As the part of programming,it is very common requirement to write and read data wrt csv
files. Python provides csv module to handle csv files.


Note: Observe the difference with newline attribute and without
with open("emp.csv","w",newline='') as f:
with open("emp.csv","w") as f:
Note: If we are not using newline attribute then in the csv file blank lines will be included
between data. To prevent these blank lines, newline attribute is required in Python-3,but
in Python-2 just we can specify mode as 'wb' and we are not required to use newline
attribute.


Zipping and Unzipping Files:
It is very common requirement to zip and unzip files.
The main advantages are:
1. To improve memory utilization
2. We can reduce transport time
3. We can improve performance.
To perform zip and unzip operations, Python contains one in-bulit module zip file.
This module contains a class : ZipFile
To create Zip file:
We have to create ZipFile class object with name of the zip file,mode and constant
ZIP_DEFLATED. This constant represents we are creating zip file.
f = ZipFile("files.zip","w","ZIP_DEFLATED")
Once we create ZipFile object,we can add files by using write() method.
f.write(filename)

To perform unzip operation:
We have to create ZipFile object as follows
f = ZipFile("files.zip","r",ZIP_STORED)
ZIP_STORED represents unzip operation. This is default value and hence we are not
required to specify.
Once we created ZipFile object for unzip operation,we can get all file names present in
that zip file by using namelist() method.
names = f.namelist()

Q1. To Know Current Working Directory:
import os
cwd=os.getcwd()
print("Current Working Directory:",cwd)
Q2. To create a sub directory in the current working directory:
import os
os.mkdir("mysub")
print("mysub directory created in cwd")


Q3. To create a sub directory in mysub directory:
cwd
|-mysub
|-mysub2
import os
os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")

To remove multiple directories in the path:
import os
os.removedirs("sub1/sub2/sub3")
print("All 3 directories sub1,sub2 and sub3 removed")

To rename a directory:
import os
os.rename("mysub","newdir")
print("mysub directory renamed to newdir")

To know contents of directory:
os module provides listdir() to list out the contents of the specified directory. It won't
display the contents of sub directory.

Q. What is the difference between listdir() and walk() functions?
In the case of listdir(), we will get contents of specified directory but not sub directory
contents. But in the case of walk() function we will get contents of specified directory and
its sub directories also.

How to get information about a File:
We can get statistics of a file like size, last accessed time,last modified time etc by using
stat() function of os module.
stats = os.stat("abc.txt")
The statistics of a file includes the following parameters:
st_mode==>Protection Bits
st_ino==>Inode number
st_dev===>device
st_nlink===>no of hard links
st_uid===>userid of owner
st_gid==>group id of owner
st_size===>size of file in bytes
st_atime==>Time of most recent access
st_mtime==>Time of Most recent modification
st_ctime==> Time of Most recent meta data change


Note:
st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st
1970 ,12:00AM. By using datetime module fromtimestamp() function,we can get exact
date and time.


The process of writing state of object to the file is called pickling and the process of
reading state of an object from the file is called unpickling.
'''


# l=[1,2,3,4,5]
# l.insert(0,4)
# print(l)

def simple():
    for i in range(10):
        if(i%2==0):
             yield i



# for num in range(-2,5,1):
#     print(num,end=',')


'''
'''