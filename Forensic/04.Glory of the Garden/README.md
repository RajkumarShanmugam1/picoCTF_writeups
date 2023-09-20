# Glory of the Garden

## Description
- This [garden](./garden.jpg) contains more than it seems.
- Author: jedavis/Danny
- Tags  : picoCTF2021 , Forensics
- Source: [garden](./garden.jpg)

<ins>Step - 1</ins> :
- Download The source file
- First i try to see the meta data of the file .
- But not use so go to next for chenk binary content using `binwalk` that was not help.

<ins>Step - 2</ins>:
- Finally see a content of file using `Strings` comment.
   ```sh
   sudo strings garden.jpg | grep "pico"
   ```
- Finally i got the flag `picoCTF{****}`
