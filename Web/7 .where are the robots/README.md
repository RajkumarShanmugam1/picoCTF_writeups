# where are the robots

## Description
- Can you find the robots? https://jupiter.challenges.picoctf.org/problem/56830/ ([link](./http://jupiter.challenges.picoctf.org:56830)) or http://jupiter.challenges.picoctf.org:56830
- Author: zaratec/Danny
- Tags  : picoCTF2021 , WebExploit
- Source: [URL](http://mercury.picoctf.net:15614/)

<ins>Approach</ins>
- Open the [URL](http://mercury.picoctf.net:15614/).
- In the site have a question `Where are the robots?`.
- Enter `robot.txt` on the end of file.
![image](https://user-images.githubusercontent.com/76644058/210207516-d58143a5-17e8-4102-a999-6e4009889bb0.png)
- Then open https://jupiter.challenges.picoctf.org/problem/56830/robots.txt
- Which site have a rule 
  ``` 
  User-agent: *
  Disallow: /1bb4c.html
  ```
- So Search the 1bb4c.html file .
![image](https://user-images.githubusercontent.com/76644058/210207569-317b4d32-a991-48b4-b311-9880566e1fda.png)
- Then open https://jupiter.challenges.picoctf.org/problem/56830/1bb4c.html
![image](https://user-images.githubusercontent.com/76644058/210208038-7488977f-fb03-44d8-aeed-c5b78965e5b3.png)
- Finally the flag is here.
