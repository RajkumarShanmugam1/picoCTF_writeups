# Transformation

## Description
- None
- Author: syreal
- Tags  : picoCTF2021 , Reverse Engineering
- Source: [crackme.py](./crackme.py)

This is simple python 

<ins> Step - 1 <ins>:
- Then i run the python program.
  ```python
  python3 crackme.py
  ```
- output : 
  ```
  What's your first number? 1
  What's your second number? 2
  The number with largest positive magnitude is 2
  ```
  
<ins> Way - 2 <ins>:
- That was not help full me . So look the content of file  
  
  ```
  # Hiding this really important number in an obscure piece of code is brilliant!
  # AND it's encrypted!
  # We want our biggest client to know his information is safe with us.
  bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"
  ```
- Which content are present in starting of program . 
- This can be decrypted using the `decode_secret` method BUT the method is never called.
- I replaced the call for `choose_greatest()` on line 34 for `decode_secret(bezos_cc_secret)` and ran it.
  ```python
  python3 crackme.py
  ```
