# PW Crack 2

## Description
- Can you crack the password to get the flag? Download the password checker [here](./level1.py) and you'll need the encrypted [flag](./level1.flag.txt.enc) in the same directory too.
- Author: Sanjay C/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: [level2.py](level2.py) , [level2.flag.txt.enc](./level2.flag.txt.enc)

<ins>Approach</ins> :
- Install the python on you system and learn python using [greeks](./https://www.geeksforgeeks.org/python-programming-language/) .
- Run this python program using uder noted command.
   ```python
   python level2.py level2.flag.txt.enc
   ```
- The program needed for password , So i check the python file full.
- Line number 18 of the python file have the password.
- But which is ascii number . When i convert the normal using python3
- Finally i got the flag `picoCTF{Your_Ouput}`

![image](https://user-images.githubusercontent.com/76644058/207778420-675ddb0a-944c-4ee7-ad3d-741e98b4ef11.png)
