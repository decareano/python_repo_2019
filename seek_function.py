#!/usr/bin/python3

fo = open("foo.txt", "r+")
print("name of file: ", fo.name)

line = fo.readlines()
print("read line: %s " % (line))

fo.seek(0)
line = fo.readline()
print("read line: %s " % (line))
fo.close()
