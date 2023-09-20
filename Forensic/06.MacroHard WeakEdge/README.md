# MacroHard WeakEdge

## Description
- I've hidden a flag in this file. Can you find it? Forensics is [fun.pptm](./fun.pptm)
- Author: madStacks
- Tags  : picoCTF2021 , Forensics
- Source:  [fun.pptm](./fun.pptm)

<ins>approach</ins>
- First open presention.
- There was no contents in slides.
- So check the binary content in presentation using `binwalk`
	```sh
	binwalk -e fun.pptm
	```
- So hidden folder is extracted in the name of `_fun.pptm.extracted`
- In the folder `_fun.pptm.extracted\ppt\slideMaters\` have `hidden` file
![image](https://user-images.githubusercontent.com/76644058/210968335-9010f317-c7e7-449b-87e4-eb8150dd36b4.png)
- The content of hidden is 
	> Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
- Then i remove the space and decode the text using base64
![image](https://user-images.githubusercontent.com/76644058/210968597-cb65fa84-f0cf-4042-9778-e173787d3a23.png)
