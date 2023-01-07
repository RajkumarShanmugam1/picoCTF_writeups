# Trivial Flag Transfer Protocol

## Description
- Figure out how they moved the flag.
- Author: Danny
- Tags  : picoCTF2021 , Forensics
- Source: tftp.pcapng

<ins>approach</ins>
- The source file is the pcapng file .That is network capturing file.
- Open the the source file in the [wireshark-tool](www.wireshark.org).
- The source file have log og lot of file exchange using TFTP
![image](https://user-images.githubusercontent.com/76644058/211133157-63b7e9ba-ae09-4c45-b281-07ed69f9bbd0.png)
- So Export thus object files using `File > Export Object > TFTP` and click saveall open in your particular folder.
![image](https://user-images.githubusercontent.com/76644058/211133186-dc82f68a-29fc-4860-925e-bb9a320d2584.png)
- First explore the `instruction.txt` which have the some encrypted text.
![image](https://user-images.githubusercontent.com/76644058/211133210-ed87020c-376d-4df6-b179-ec7d08b3741b.png)
- Content of instruction.txt 
  > GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA  
- Now decrypt by subtitution method like ceasar cipher, ROT , etc... 
- The [ROT13](https://rot13.com/) is decrypt this text.
![image](https://user-images.githubusercontent.com/76644058/211133228-5581bba3-194a-41d3-833e-5e752e166dcc.png)
- The Result is :
	> TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN  
- Please identified the sentences using separation. After Separate :
	> TFTP DOESNT ENCRYPT OUR TRAFFIC SOWE MUST DISGUISE OUR FLAG TRANSFER.FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECKBACK FOR THE PLAN  
- Second check the `plan` file. Which have another encrypted data.
![image](https://user-images.githubusercontent.com/76644058/211133257-59725b8e-e58a-4b09-827a-baa531b8c01d.png)
- Please follow last method to decrypt.
	> VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
- Decrypted data:
	> I USED THE PROGRAM AND HID IT WITH- DUEDILIGENCE. CHECK OUT THE PHOTOS  
- Then install the program.dep file 
	```sh
	sudo dpkg -i  program.dep
	```
![image](https://user-images.githubusercontent.com/76644058/211133273-04cec030-da7b-43d2-9192-d43a7ab3aee4.png)
- Which program have `steghide` tool for retrive the data from 3 photos.Which is concept known as stegnography.
- The password for `DUEDILIGENCE` from plan file
	```
	sudo steghide extract -sf <filename>
	```
![image](https://user-images.githubusercontent.com/76644058/211133332-50b3053d-89c4-455c-bfe8-e4fa15e2d4ff.png)
- Finally the flag is present in flag.txt file.
