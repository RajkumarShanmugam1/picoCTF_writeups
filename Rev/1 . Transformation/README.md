# Transformation

## Description
- I wonder what this really is... [enc](https://github.com/Sriraj151/picoCTF_writeups/edit/main/Rev/1%20.%20Transformation/enc). `join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
- Author: madStacks
- Tags  : picoCTF2021 , Reverse Engineering
- Source: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ

I guess this is encode format . Like ` ISCII , UIF ` . So i try to decode the message , WHen i got the Flag.

<ins> Way - 1 <ins>:
- First i try to decode the message with a help of [`Cyper-chef`](https://gchq.github.io/CyberChef/).
![image](https://user-images.githubusercontent.com/76644058/201001158-35b36c23-73ce-4a42-acb9-93786cd3f798.png)

- Use Encode Message , UTF-163E option.
![image](https://user-images.githubusercontent.com/76644058/201001404-9079d411-e760-4570-9e89-80b36b70b733.png)

<ins> Way - 2 <ins>:
- I try to decode in the of python code , Which available in this folder .
![image](https://user-images.githubusercontent.com/76644058/201020039-af3127a2-1a12-47ca-94ce-bd8871c9fd9b.png)
