# Cookies

## Description
- Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:17781/
- Author: madStacks
- Tags  : picoCTF2021 , WebExploit
- Source: [URL](http://mercury.picoctf.net:17781/)

<ins>Step - 1</ins> :
  - The link goes to something that looks like this:
  ![image](https://user-images.githubusercontent.com/76644058/200643094-c4f08f6d-8c59-488b-b00e-fe127c6bb9f0.png)
  - Then I typed in "snickerdoodle" and entered it.
  - - So Now i guess to check the cookie value.
  
<ins>Step - 2<ins>:
  - Inspect the web page and Go to the Storage option.
      - Shortcut : ```sh
                   Ctrl + Shift + I
                   ```
 
<ins>Step - 3<ins>:
  - Find cookies storage . Change the value of cookie `0` -> `1`
  - output : 
  ![image](https://user-images.githubusercontent.com/76644058/200643094-c4f08f6d-8c59-488b-b00e-fe127c6bb9f0.png)
  
<ins>Step - 4<ins>:
  - Change the value `1` to `18`
  - Finally i got the flag in cookie value of 18
