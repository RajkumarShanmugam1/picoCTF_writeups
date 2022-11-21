# Magikarp Ground Mission

## Description
- Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6d448c9c`
- Author: syreal
- Tags  : picoCTF2021 , General skills
- Source: None


Hmm start by connecting to the server with `ssh ctf-player@venus.picoctf.net -p 50713` and `6d448c9c` as the password like the question says.

<ins>Step - 1</ins>:

- Using `ls` lists `1of3.flag.txt  instructions-to-2of3.txt`
- With `cat 1of3.flag.txt`, we get
  ```text
     picoCTF{xxsh_
  ```

<ins>Step - 2</ins>:
- ```sh
   cat instructions-to-2of3.txt
   ```
   ```text
      Next, go to the root of all things, more succinctly `/`
   ```

<ins>Step - 3</ins>:
- SO i typed in `cd ..` (go back a directory) then `ls -a` (list all because I have trust issues with hidden files) and came across `3of3.flag.txt`
  ```sh
  cat 3of3.flag.txt
  ```
  ```text
    5190b070}
  ```

<ins>Step - 4</ins>:
- I kept going back (with `cd ..`) and listing the files and directories (`ls -a`) until `2of3.flag.txt` appeared.
- ```sh
  cat 2of3.flag.txt
  ```
  ```text
    0ut_0f_\/\/4t3r_
  ```

<ins>Step - 5</ins>:
- Connected this parts of flag 
