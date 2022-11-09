# Insp3ct0r

## Description
- Kishor Balan tipped us off that the following code may need inspection: http://jupiter.challenges.picoctf.org:9670
- Author: zaratec/danny
- Tags  : picoCTF2021 , WebExploit
- Source: [URL1](https://jupiter.challenges.picoctf.org/problem/9670/)
          [URL2](http://jupiter.challenges.picoctf.org:9670)

Title is inspector , So i think inspect all pages and source of this website.
Source attached from picoCTF

<ins>Step - 1</ins> :
- Visiting the website, we right click and choose to view source code, getting the first third of the flag, included as a html comment:
  [Result](view-source:https://jupiter.challenges.picoctf.org/problem/9670/)
![image](https://user-images.githubusercontent.com/76644058/200843200-7c2393fb-e43f-4c13-818a-27964457dbbb.png)
- When i got the 1st part of flag in the 31 th line on [Source Page]()
   `<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->`
  
<ins>Step - 2</ins> :
- Then Inspect the site ` Ctrl + Shift + I ` and Click on the style editor
- I got the Second pard of flag in 51 line on [mycss.css]()
![image](https://user-images.githubusercontent.com/76644058/200843380-c2af5bda-a063-4ce5-bed3-9d569431f55e.png)
  
<ins>Step - 3</ins> :
- Then i try to access the js file like https://jupiter.challenges.picoctf.org/problem/9670/ + myjs.js
- Finall part are also catched . 
![image](https://user-images.githubusercontent.com/76644058/200843692-250771c1-af78-4ef6-904e-06ad40195c96.png)

##Thank to all
