# Waving Flag

## Description
- Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm) has extraordinarily helpful information...
- Author: syreal
- Tags  : picoCTF2021 , General skills
- Source: [warm](https://github.com/Sriraj151/picoCTF_writeups/blob/main/General_Skill/03.%20Wave%20a%20flag/warm)

They give simple ELF 64-bit LSB pie executable file . using,
```sh
file <FILE-NAME>
```
<ins>Way - 1</ins> :
- This program will only work in the webshell or another Linux computer.
- To get the file accessible in your shell, enter the following in the Terminal prompt:
```sh
wget [https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm)
```

<ins>Way - 2</ins>:

- Run this program by entering the following in the Terminal prompt
```sh
chmod +x warm
./warm
```
