# Transformation

## Description
- I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
- Author: madStacks
- Tags  : picoCTF2021 , Reverse Engineering
- Source: [chall.S](./chall.S)

## Approach
- Actually this is the some encoding format.
- So i want to decode. When i Use the utf.
