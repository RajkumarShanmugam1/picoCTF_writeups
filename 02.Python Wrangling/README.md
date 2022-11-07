# Python Wrangling

### Description
- Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
- Author: syreal
- Tags  : picoCTF2021 , General skills
- Source: [python](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py),[Password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt) , [flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)

<ins>Step - 1</ins> :
- Download The source file
- First install python3 and required packages.
     ```sh
     sudo apt-get install python
     ```
- Packages downloads
	```sh
	pip install sys
	pip install base64
	pip install cryptography
	```

<ins>Step - 2</ins>:
- copy the content in the password file
- Run the python file using brlow code
   ```sh
   python3 ende.py -d flag.txt.en
   ```
- Enter the password in the password file
- Finally i got the flag `picoCTF{****}`
