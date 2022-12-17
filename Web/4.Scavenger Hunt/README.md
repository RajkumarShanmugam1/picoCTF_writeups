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
- When i got the 1st part of flag in the 31 th line on [Source Page](./index.html)
   - `<!-- Here's the first part of the flag: picoCTF{t -->`
 
 ![image](https://user-images.githubusercontent.com/76644058/200843200-7c2393fb-e43f-4c13-818a-27964457dbbb.png)
  
<ins>Step - 2</ins> :
- Then Inspect the site ` Ctrl + Shift + I ` and Click on the style editor
- I got the Second pard of flag in 51 line on [mycss.css](./mycss.css)

![image](https://user-images.githubusercontent.com/76644058/200843380-c2af5bda-a063-4ce5-bed3-9d569431f55e.png)
  
<ins>Step - 3</ins> :
- Then i try to access the js file like `https://jupiter.challenges.picoctf.org/problem/9670/myjs.js`	
- `/* How can I keep Google from indexing my website? */` ~ Which is the last line of the myjs.js
- oh no there no flags are present.But hint is here.
- Now think that `which is used to index from google?`

![image](https://user-images.githubusercontent.com/76644058/208227942-5e0cf272-5c00-43f3-9583-73da0f4981b5.png)

<ins>Step - 4</ins>:
- `How can I keep Google from indexing my website?` ~ which is robots.txt of the webpage .
- So enter the link `http://mercury.picoctf.net:39491/robots.txt`
- The 3rd pard is here

![image](https://user-images.githubusercontent.com/76644058/208228004-e7f0de50-0dac-49b6-9c9f-16665f15aeb7.png)

<ins>Step - 5</ins>:
- Last line have hint for next flag `I think this is an apache server... can you Access the next flag?`. 
- The file `.htaccess` have the access details , SO Enter the `http://mercury.picoctf.net:39491/.htaccess`
- The 4th flag is gotted.

![image](https://user-images.githubusercontent.com/76644058/208228535-477d750c-e99c-4400-86bd-3223b87916e0.png)

<ins>Step - 6<ins>:
- Then the next hint is `I love making websites on my Mac, I can Store a lot of information there`
- The information are stored in the .DS_Store
- So Search the link `http://mercury.picoctf.net:39491/.ds_store`
- There is the final flag.

![image](https://user-images.githubusercontent.com/76644058/208228559-798178bc-3d3f-4c85-8c52-b5e81611f571.png)

# Thanks to all
