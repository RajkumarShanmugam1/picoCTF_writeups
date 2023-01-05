# Big Zip

## Description
- Unzip this archive and find the flag.[Download zip file](./big-zip-files.zip)
- Author: LT 'syreal' Jones
- Tags  : picoCTF2021 , General skills
- Source: [zip](./big-zip-files.zip)


<ins>Approach</ins> :
- Extract the zip using gui or cli .
- In GUI the option of extract is used to extract the zip file.
- Search the word `picoCTF` using grep.
- grep option `-n` using every line check.
- grep option `-r` using recursive like force .
   ```
   unzip big-zip-files.zip
   cd big-zip-files
   grep -nr picoCTF
   ```
![image](https://user-images.githubusercontent.com/76644058/210713946-258218a4-8945-41bf-9502-083e8877f322.png)
