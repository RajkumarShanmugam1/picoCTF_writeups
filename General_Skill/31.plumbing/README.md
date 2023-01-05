# plumbing

## Description
- Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to ```jupiter.challenges.picoctf.org 4427`.
- Author: Alex Fulton/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: `jupiter.challenges.picoctf.org 4427`

<ins>Approach</ins> :
- First run the command.
	```sh
	jupiter.challenges.picoctf.org 4427
	```
- Which return lot of lines.i can not find flag here
- So i save the the output of execution into a text file
- Then i search the flag in text file using grep with a keyword of `picoCTF`
- All Execution and cammands are below
	```
	nc jupiter.challenges.picoctf.org 4427 >> a.txt
	cat a.txt | grep pico
	```
