# flag_shop

## Description
- There's a flag shop selling stuff, can you buy a flag? [source](./source.c). Connect with `nc jupiter.challenges.picoctf.org 9745`.
- Author: AlDanny
- Tags  : picoCTF2021 , General skills
- Source: [source](./source.c)

<ins>Approach</ins> :
- Enter the command `nc jupiter.challenges.picoctf.org 9745` in terminal
- The reference of program is present in [source](./source.c)
- The Outputs of Teminal Command:
	```text
	Welcome to the flag exchange
	We sell flags
		1. Check Account Balance
		2. Buy Flags
		3. Exit
	Enter a menu selection 2
	Currently for sale
		1. Defintely not the flag Flag
		2. 1337 Flag
	1
	These knockoff Flags cost 900 each, enter desired quantity
	1234567890
	The final cost is: -1285428664
	Your current balance after transaction: 1285429764

	Welcome to the flag exchange
	We sell flags
		1. Check Account Balance
		2. Buy Flags
		3. Exit
	Enter a menu selection 2
	Currently for sale
		1. Defintely not the flag Flag
		2. 1337 Flag
	2
	1337 flags cost 100000 dollars, and we only have 1 in stock
	Enter 1 to buy one 1
	YOUR FLAG IS: picoCTF{m0n3y_bag5_65d67a74}	
	```
- First the Balance is $1100
- In the program,
  ```c
  if(number_flags > 0){
         int total_cost = 0;
         total_cost = 900*number_flags;
         printf("\nThe final cost is: %d\n", total_cost);
         if(total_cost <= account_balance){
                 account_balance = account_balance - total_cost;
                 printf("\nYour current balance after transaction: %d\n\n", account_balance);
         }
  ```
- Which changes the account balance.
- Then buy the flag
