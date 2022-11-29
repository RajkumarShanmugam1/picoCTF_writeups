# First Grep

## Description
- Can you find the [flag](./file) in file? This would be really tedious to look through manually, something tells me there is a better way.
- Author: Alex Fulton/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: [file](./file)

<ins>Approach</ins> :
- First i want to known the type of the file.
  - Command :
    - ```sh
      file file
      ```
    - Result :`file: ASCII text, with very long lines`
- Show  i try to see the content of pico int file using `cat`
  - Command:
     - ```sh
       cat file | grep "pico"
       ```
     - Result : Which return the correct flag.
- Finally i got the flag `picoCTF{xxx_xxx_...}`
