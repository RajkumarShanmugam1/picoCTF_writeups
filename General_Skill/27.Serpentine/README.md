# Serpentine

## Description
- Find the flag in the Python script! [Download](./serpentine.py) Python script
- Author: LT 'syreal' Jones
- Tags  : picoCTF2021 , General skills
- Source: [serpentine.py](./serpentine.py)

<ins>Approach</ins> :
- Install the python on you system and learn python .
- Run this python program using uder noted command.
   ```python
   python serpentine.py
   ```
- The Menus have `[a. Print encouragement , b) Print flag, c) Quit ]` - options.
- But the option of `b` returns `Oops! I must have misplaced the print_flag function! Check my source code!`.
- So call the `print_flag()` function in line 69 of script file.

![image](https://user-images.githubusercontent.com/76644058/208067568-003c23b6-873a-47f1-b19d-5f9de0a90d2c.png)

- Then run the python file

![image](https://user-images.githubusercontent.com/76644058/208067746-ba7c4eea-03fa-4c9c-a8d6-4138821bb8ac.png)

- The flag is the output of the script.
