# PW Crack 4

## Description
- Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.
- Author: Sanjay C/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: [level3.py](level3.py) , [level3.flag.txt.enc](./level3.flag.txt.enc)

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
![image](https://user-images.githubusercontent.com/76644058/207781607-32ed9c1a-b9dd-4994-872c-0baea08448be.png)
