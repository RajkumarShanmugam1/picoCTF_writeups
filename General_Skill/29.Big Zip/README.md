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
   ```
   unzip big-zip-files.zip
   cd big-zip-files
   grep -nr picoCTF
   ```
