# tunn3l v1s10n

## Description
- Files can always be changed in a secret way. Can you find the flag?.
- Author: susie
- Tags  : picoCTF2021 , Forensics
- Source: cat.jpg

We found this [file](./tunn3l_v1s10n). Recover the flag.

<ins>approch</ins>
- There is no [file extension](https://en.wikipedia.org/wiki/Filename_extension).so we don't actually know what type of file it is.
![image](https://user-images.githubusercontent.com/76644058/210198691-70d0a3ff-e397-4ec0-a284-15660e678776.png)

- Let's open this with a online-hex-editor like [hex-works](https://hex-works.com/eng) to check the intended file type. 
- The first two characters are `BM` which indicates a BMP file.
![image](https://user-images.githubusercontent.com/76644058/210198902-197d9704-029e-4c3a-8b24-f29e3b4b0b90.png)

- Let's change the file extension to `.bmp` and since it still doesn't open
![image](https://user-images.githubusercontent.com/76644058/210198998-674c29c3-3140-45ce-8c99-d53081296bac.png)

- I decided to use [OnlineImageMagick](https://magickstudio.imagemagick.org/scripts/MagickStudio.cgi) to open it. 
- I'm sure there's probably some way of changing the file header to open it properly but that's alright. It displays:
![image](https://user-images.githubusercontent.com/76644058/210199221-e5e7b868-352f-4b15-81bb-b325d7dc2d0f.png)

- Something interesting to note is the size of the BMP file. It's about 2MB in size for such a tiny image? That doesn't seem right. [This site](http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm) explains what everything in the BMP header is.

- Height for a BMP file is at [offset](http://www.novell.com/documentation/ndsv8/usnds/c1help/novell_common/hexeditor.html) 0016h. I changed offset 0017h from 0x01 to 0x03.
