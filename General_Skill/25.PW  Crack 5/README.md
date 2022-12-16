# PW Crack 4

## Description
- Can you crack the password to get the flag? Download the password checker [here](./level5.py) and you'll need the encrypted [flag](./level5.flag.txt.enc) and the [hash](./level5.hash.bin) in the same directory too. There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.
- Author: Sanjay C/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: [level5.py](level5.py) , [level5.flag.txt.enc](./level5.flag.txt.enc) , [level5.hash.bin](./level5.hash.bin)

<ins>Approach</ins> :
- Install the python on you system and learn python using [greeks](https://www.geeksforgeeks.org/python-programming-language/) .
- Run this python program using uder noted command.
   ```python
   python3 level4.py level4.flag.txt.enc level4.hash.bin
   ```
- The program needed for password , So i check the python file full.
- Line number 45 of the python file have possibilities of 200 password5.
- So i create the password_checking [program](./check_pw.py).
- But which is ascii number . When i convert the normal using python3
- Finally i got the flag `picoCTF{Your_Ouput}`
