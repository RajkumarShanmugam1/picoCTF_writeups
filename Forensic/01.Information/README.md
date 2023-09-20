# Information

## Description
- Files can always be changed in a secret way. Can you find the flag?.
- Author: susie
- Tags  : picoCTF2021 , Forensics
- Source: cat.jpg

<ins>Step - 1</ins> :
- Download The source file
- First check File Type
   ```sh
   file flag
   ```
<ins>Step - 2</ins>:
- Show the metadata of the file using exiftool
   ```sh
   sudo apt-get install exiftool
   
   exiftool cat.jpg
   ```

<ins>Step - 3</ins>:
- I saw the license of this jpg in the form base64 encryption
- So i try the to decrypt the licence value
  ```sh
  echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
  ```
- Finally i got the flag `picoCTF{****}`
