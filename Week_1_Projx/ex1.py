from os import listdir, chdir
from os.path import exists
from shutil import move

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
	"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

chdir("files")
direcFiles = listdir(".")

for fileName in direcFiles:
	for letter in alphabet:
		if fileName.startswith(letter):
			if exists("files/", letter):
				# move it without overriding
			else:
				fileName.move(".", ("./%s" % letter)) # is this way of writing the dest better?!
		else:
			continue


# get list of files
# loop:
# 	set variable to first letter of file name
#	check if directory exists with that variable name
#	if no, 
#		move file into that directory
#		called ".//%s//" % x
#	if yes
#		what the heck, how do we move it 
