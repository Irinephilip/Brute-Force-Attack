# Brute-Force-Attack
Crack Hashed Passwords from a File Using Brute Force

Project Summary: Brute-Force Cracking Hashed Passwords from a File
🎯 Objective
To simulate a real-world brute-force attack by writing a Python script that:

Reads username and hashed password pairs from a file

Compares those hashes with values generated from a wordlist

Cracks passwords by matching hashes with guessed values

This project mimics how attackers use hash lists from data breaches and attempt to recover passwords offline.

Tools & Technologies Used
Tool	Purpose
Python	Core scripting language
hashlib	For generating MD5 hashes
Wordlist file	Set of common passwords to try
Hash file	Simulated user database with hashed passwords

Files Created
File Name	Description
brute-crack.py	Main Python script for the brute-force logic
hashes.txt	Contains username:hashed_password entries
wordlist.txt	Contains possible password guesses (wordlist)
README.md	Project documentation for GitHub

 How the Script Works
Reads each username:hash line from hashes.txt

Reads possible passwords from wordlist.txt

Hashes each password using MD5

Compares it to each user’s hash

Prints out the cracked password if a match is found
