# 1_wanna_b3_a_r0ck5tar

## Description
- I wrote you another [song](./lyrics.txt). Put the flag in the picoCTF{} flag format
- Author: Alex Bushkin
- Tags  : picoCTF2021 , General skills
- Source: [song](./lyrics.txt)

```diff
- > The Rockstar language has changed since this problem was released! Use this Wayback Machine URL to use an older version of Rockstar, [here](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online).
```
<ins>Approach</ins> :
- First open the RockStar Compiler

- This time the program requires some input. We can simply remove these input checks to get to the flag.
- Remove these lines:
	```text
	Listen to the music             
	If the music is a guitar                  
	...
	Else Whisper "That ain't it, Chief"

	```
- Output:
	```ascii
	66
	79
	78
	74
	79
	86
	73
	```
- Converting it to ASCII:
- The ascii values are present inside of picoCTF{xxx} .
