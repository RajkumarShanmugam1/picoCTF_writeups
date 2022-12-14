# Glitch Cat

## Description
- Our flag printing service has started glitching! - `$ nc saturn.picoctf.net 65353` .
- Author: LT 'syreal' Jones
- Tags  : picoCTF2021 , General skills
- Source: `$ nc saturn.picoctf.net 65353`

<ins>Approach</ins> :
- Enter command :
     - `nc saturn.picoctf.net 65353`
- The output is octal code or ascii value.
- Then convert the ascii -> normal value using python.
     ```python
     python3
     >>> <Enter_output_of_NetCat_(NC)>
     ```
 ![image](https://user-images.githubusercontent.com/76644058/207605198-fa54f42b-39e5-4a69-b146-0b2c4f375adb.png)

- Finally output is flag the flag `picoCTF{Your_Ouput}`
