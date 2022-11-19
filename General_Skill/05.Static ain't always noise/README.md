# Obedient Cat

## Description
- Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static)? This [BASH](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh) script might help!
- Author: syreal
- Tags  : picoCTF2021 , General skills
- Source: ltdis.sh , static

I guess this is shell scripting. so i can view and run the static els files
<ins>Way - 1</ins> :
- Download The source file
- Run the static executable file using ltdis.sh
```sh
chmod +x ltdis.sh
./ltdis.sh static
```
- The Result is : (static.ltdis.txt named file is created)
> Attempting disassembly of static ...
> Disassembly successful! Available at: static.ltdis.x86_64.txt
> Ripping strings from binary with file offsets...
> Any strings found in static have been written to static.ltdis.strings.txt with file offset

- After view the content of file When i got the flag .
```sh
cat static.ltdis.strings.txt | grep "pico"
```

<ins>Way - 2</ins>:
- view the executable file (static) content
```sh
cat static.ltdis.strings.txt | grep "pico"
```

> Finally i got the flag `picoCTF{****}`
