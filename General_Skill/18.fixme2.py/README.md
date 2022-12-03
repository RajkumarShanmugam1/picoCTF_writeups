# fixme2.py

## Description
- Fix the syntax error in this Python script to print the flag.
- Author: LT 'syreal' Jones
- Tags  : picoCTF2021 , General skills
- Source: [fixme2.py](./fixme2.py)

<ins>Approach</ins> :
- - Run the file using `fixme2.py`.
- Commands:
    ```sh
    sudo apt-get install python
    chmod +x fixme1.py
    python3 fixme1.py
    ```
    Result:
      ```
       File "fixme2.py", line 22
    if flag = "":
SyntaxError: invalid syntax
      ```
      
- Fix the `==` operator in line 22
- Can execute the code 
- CommandS:
     ```sh
    python3 fixme2.py
    ```
    Result:
       
       ```
       That is correct! Here's your flag: xxxxx```


- Finally i got the flag `picoCTF{Your_Ouput}`
