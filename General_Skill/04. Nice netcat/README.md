# Nice netcat

## Description
- There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 43239, but it doesn't speak English...
- Author: syreal
- Tags  : picoCTF2021 , General skills
- Source: link

<ins>Step - 1</ins> :
- First I connected to `mercury.picoctf.net 43239` on a Linux terminal.
- It gave these numbers:
   > 112
   105
   99
   111
   67
   84
   70
   123
   103
   48
   48
   100
   95
   107
   49
   116
   116
   121
   33
   95
   110
   49
   99
   51
   95
   107
   49
   116
   116
   121
   33
   95
   55
   99
   48
   56
   50
   49
   102
   53
   125
   10


<ins>Step - 2</ins>:
- These numbers are most likely ASCII values for text. 
- I got tired of trying to look for an online source to decode it. I tried about 3 and they all didn't work. I wrote up a Python script

```python
nums = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 55, 99, 48, 56, 50, 49, 102, 53, 125, 10]
flag = ""
for number in nums:
    flag += chr(number)
print(flag)
```
- Finally i got the flag `picoCTF{****}`
