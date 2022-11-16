# [Pico CTF](https://picoctf.org)
## Writeups and Learnings

## [About](https://picoctf.org/about.html)
- The largest high school hacking competition now provides year-round cyber security education content for learners of all skill levels.< /br>

- Participants learn to overcome sets of challenges from six domains of cybersecurity including general skills, cryptography, web exploitation, forensics, etc. The challenges are all set up with the intent of being hacked, making it an excellent, legal way to get hands-on experience. 

## Categories :
- Web Exploitation
- Cyptography
- Reverse Engineering
- Forensics
- Binary Exploitaions 
- General Skills

<center><img src="https://user-images.githubusercontent.com/76644058/200155642-d4f67368-0b9d-4a4e-8926-7884d4b118d5.png" width="300" /></center>

---

## Requirements :
- Operating Systems like [Kali linux , Parrot OS , etc ...]
- Normal performance laptop like (Ram : 4GB , Storage : 50GB , )

## Knowledge Need and Improved :
- Cyptography
- Web Technologies
- Networks
- Binary Exploitaions 
- Reverse Engneering
- Stegnography
- OSINT
- Linux

> **[CTF Knowledge](https://github.com/Sriraj151/CTF-Practice-and-Training)**


# crackme-py

## Description

[crackme.py](./crackme.py)

## Hints

(None)

## Approach

When looking at the contents of the Python file, there are a few things to note:

```python
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"
```

This can be decrypted using the `decode_secret` method BUT the method is never called.
I replaced the call for `choose_greatest()` on line 34 for `decode_secret(bezos_cc_secret)` and ran it.

## Flag

picoCTF{1|\/|_4_p34|\|ut_dd2c4616}
