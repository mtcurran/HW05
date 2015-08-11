#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
import os
# Body

def print_gt20s():
	wordlist = open("words.txt", "r")
	for line in wordlist:
		if len(line.strip(" ")) > 20:
			print line
	wordlist.close


##############################################################################
def main():
    
    print_gt20s()

if __name__ == '__main__':
    main()
