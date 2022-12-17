# Scavenger Hunt

## Description
- There is some interesting information hidden around this site http://mercury.picoctf.net:39491/. Can you find it?
- Author: madStacks
- Tags  : picoCTF2021 , WebExploit
- Source: [URL](http://mercury.picoctf.net:39491/)

This is also inspector , So i think inspect all pages and source of this website.Source attached from picoCTF

<ins>Step - 1</ins> :
- Visiting the website, we right click and choose to view source code, getting the first third of the flag, included as a html comment:
  [Result](view-source:http://mercury.picoctf.net:39491/)
![image](https://user-images.githubusercontent.com/76644058/200843200-7c2393fb-e43f-4c13-818a-27964457dbbb.png)
- When i got the 1st part of flag in the 31 th line on [Source Page](./index.html)
   - `<!-- Here's the first part of the flag: picoCTF{t -->`
  
<ins>Step - 2</ins> :
- Then Inspect the site ` Ctrl + Shift + I ` and Click on the style editor
- I got the Second pard of flag in 51 line on [mycss.css](./mycss.css)
- 
![image](https://user-images.githubusercontent.com/76644058/200843380-c2af5bda-a063-4ce5-bed3-9d569431f55e.png)
  
<ins>Step - 3</ins> :
- Then i try to access the js file like `https://jupiter.challenges.picoctf.org/problem/9670/myjs.js`	
- `/* How can I keep Google from indexing my website? */` ~ Which is the last line of the myjs.js
- Now think that `which is used to index from google?`

<ins>Step - 4</ins>:
- `How can I keep Google from indexing my website?` ~ which is robots.txt of the webpage .
- So enter the link `http://mercury.picoctf.net:39491/robots.txt`
- The 3rd pard is here

# Thanks to all
