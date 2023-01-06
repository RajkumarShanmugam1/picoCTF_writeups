# Mind your Ps and Qs

## Description
- In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [value](./vlaues)
- Author: Sara
- Tags  : picoCTF2021 , Cryptography
- Source: [value](./vlaues)

<ins>RSA Algorithm</ins> :
- RSA Algorithm:
	- Values :
		> Given or take the values `p , q` - Two Prime numbers , `m` - Message
		> i  . Find the value of `n = p * q`
		> ii . Find the value of `phi = (p-1)*(q-1)`
		> iii. Find the value of `e` from  `gcd (e,phi) =1` [private key]
		> iv . Find the value of `d = de mod φ (n)` [Public key] 
	- Encryption:
		> c = (m^e) mod n
	- Decryption:
		> m = (c^d) mod n
- The given values are,
	```text
	c: 240986837130071017759137533082982207147971245672412893755780400885108149004760496
	n: 831416828080417866340504968188990032810316193533653516022175784399720141076262857
	e: 65537
	```

<ins>Approach</ins>
- Only decrypt the message from the given data.
- The need values of decryption is c , d , n
- c , n is already given
- The p , q are factors of n that find from the [factorDB](www.factordb.com). 
- Then create the [script](./script.py) for RSA decrytion.
