# Matryoshka doll

## Description
- Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [Source]()
- Author: Susie/Pandu
- Tags  : picoCTF2021 , Forensics

I guess this is image-stegnography.

<ins>Step - 1</ins> :
- First check the binary details of file using binwalk .
     ```sh
     sudo binwalk -e filename
     ```
- Which command using to extract the binary files in source file . 
- The extracted file name is _Realfile_name

<ins>step -2<ins>:
-Until repeated the step-1 when got the text file`flag.txt`.
-Which have some message .

<ins>step -2<ins>:

Waiting for updation
