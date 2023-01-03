# ARMssembly 0

## Description
- What integer does this program print with arguments `182476535` and `3742084308`? File: [chall.S](./chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
- Author: Dylan McGuire
- Tags  : picoCTF2021 , Reverse Engineering
- Source: [chall.S](./chall.S)

<ins>Understanding the basics</ins>:

- I would say that I am somewhat comfortable with classic `x86` assembly, but I had to learn about `ARM` for this challenge (which I love! Learning new stuff is more than cool). So we can break down the first function, step by step:
```arm
func1:
	sub	sp, sp, #16  
	str	w0, [sp, 12]  
	str	w1, [sp, 8]  
	ldr	w1, [sp, 12] 
	ldr	w0, [sp, 8]   
	cmp	w1, w0       
	bls	.L2          
	ldr	w0, [sp, 12] 
	b	.L3
```
- So here we go. `sp` stands for the stack pointer, and the `sub` instruction is a substraction with three components:
```
sub x,y, #z
```
- Substract `#z` (# denotes a constant value) fro `y` and store it in `x`. Why is this instruction even here? It makes space on the stack for variables, and since we have two, substracting `16` should be just enough. In the next two lines we have some essential instructions:
```
str	w0, [sp, 12]  
str	w1, [sp, 8]
```
- `str` stands for `store`, and `w0` and `w1` are the user input variables. So we `store` the values in `w0` and `w1`  on the stack (`sp`). The number denotes the offset on the stack. So `str	w0, [sp, 12]` means `store w0 on the stack at offset 12`. Pretty neat.
```
ldr	w1, [sp, 12] 
ldr	w0, [sp, 8]
```
- Here we load the values from the stack at a given offset into a variable. So `load the value at offset 12 on the stack into w1` is equal to `ldr w1, [sp, 12]`. Also neat! And very important.
```
cmp	w1, w0
``` 
- Compare the values by substracting `w0` from `w1`. So basically a `sub` except that we do not store the value. Next!
```
bls .L2
```
- Right, this is a `branch if less` instruction, if `w0` is smaller than `w1` `branch` or `jl` (for the x86 guys) to `.L2`. And at the end load a value again and `b` (simple branch `jmp` in x86). Very nice! 

<ins>Approach</ins> :

- Under the remaining functions with your self.
- In the question `182476535` and `3742084308` arguments are denote as `w0` and `w1`.
- So we change the decimal value to Hexadecimal value of `w0` using [converter](https://www.rapidtables.com/convert/number/decimal-to-hex.html)
