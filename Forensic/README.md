# Trivial Flag Transfer Protocol

## Description
- Figure out how they moved the flag.
- Author: Danny
- Tags  : picoCTF2021 , Forensics
- Source:  [tftp.pcapng](./tftp.pcapng)

<ins>approach</ins>
- The source file is the pcapng file .That is network capturing file.
- Open the the source file in the [wireshark-tool](www.wireshark.org).
- The source file have log og lot of file exchange using TFTP
- So Export thus object files using `File > Export Object > TFTP` and click saveall open in your particular folder.
- First explore the `instruction.txt` which have the some encrypted text.
- Content of instruction.txt 
  > GSGCQBRFAGRAPELCGB HEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA  
- Now decrypt by subtitution method like ceasar cipher, ROT , etc... 
- The [ROT13](https://rot13.com/) is decrypt this text.
- The Result is :
	> TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN  
- Please identified the sentences using separation. After Separate :
	> TFTP DOESNT ENCRYPT OUR TRAFFIC SOWE MUST DISGUISE OUR FLAG TRANSFER.FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECKBACK FOR THE PLAN  
- Second check the `plan` file. Which have another encrypted data.
- Please follow last method to decrypt.
	> VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
- Decrypted data:
	> I USED THE PROGRAM AND HID IT WITH- DUEDILIGENCE. CHECK OUT THE PHOTOS  
- Then install the program.dep file 
	```sh
	sudo dpkg -i  program.dep
	```
- Which program have `steghide` tool for retrive the data from 3 photos.Which is concept known as stegnography.
- The password for `DUEDILIGENCE` from plan file
	```
	sudo steghide extract -sf <filename>
	```
- Finally the flag is present in flag.txt file.
