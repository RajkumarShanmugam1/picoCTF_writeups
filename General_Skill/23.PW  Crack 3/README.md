# PW Crack 3

## Description
- Can you crack the password to get the flag? Download the password checker [here](./level3.py) and you'll need the encrypted [flag](./level3.flag.txt.enc) and the [hash](./level3.hash.bin) in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.
- Author: Sanjay C/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: [level3.py](level3.py) , [level3.flag.txt.enc](./level3.flag.txt.enc) , [level3.hash.bin](./level3.hash.bin)

<ins>Approach</ins> :
- Install the python on you system and learn python using [greeks](https://www.geeksforgeeks.org/python-programming-language/) .
- Run this python program using uder noted command.
   ```python
   python3 level3.py level3.flag.txt.enc level3.hash.bin
   ```
- The program needed for password , So i check the python file full.
- In the last line of the python program have a 8 ties of passwords.Try all passwords.
- Finally i got the flag `picoCTF{Your_Ouput}`

![image](https://user-images.githubusercontent.com/76644058/207778707-b3a7ef77-f1b1-416e-b899-b68f5828e243.png)
