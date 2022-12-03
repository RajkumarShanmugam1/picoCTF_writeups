# fixme1.py

## Description
- Fix the syntax error in this Python script to print the flag.
- Author: LT 'syreal' Jones
- Tags  : picoCTF2021 , General skills
- Source: [fixme1.py](./fixme1.py)

<ins>Approach</ins> :
- - Run the file using `fixme1.py`.
- This is number convertion quiz / game.
- Commands:
    ```sh
    sudo apt-get install python
    chmod +x fixme1.py
    python3 fixme1.py
    ```
    Result:
    
      ```
      File "fixme1.py", line 20
       print('That is correct! Here\'s your flag: ' + flag)
      IndentationError: unexpected indent
      ```
      
- After enter the backspace in the line 20.
- Can execute the code 
- CommandS:
     ```sh
    python3 fixme1.py
    ```
    Result:
       
       ```
       That is correct! Here's your flag: xxxxx
       ```


- Finally i got the flag `picoCTF{Your_Ouput}`
