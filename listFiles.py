#!/usr/bin/python
import os
import fnmatch
stream = open("Recipes.tex", "w")
for chapter in sorted(fnmatch.filter(os.listdir("recipes"), "*.tex")):
    stream.write("\\input{recipes/%s}\n" % chapter)
stream.close()