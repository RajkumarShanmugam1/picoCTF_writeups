# vault-door-training

## Description
- Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](./VaultDoorTraining.java)
- Author: Mark E. Haase
- Tags  : picoCTF2021 , Reverse Engineering
- Source: [VaultDoorTraining.java](./VaultDoorTraining.java)

## Approach
![image](https://user-images.githubusercontent.com/76644058/215389376-44bd1857-7c76-404a-9317-2c5188fdd0d3.png)
- Which is java based task.So we need a knowlege in a JAVA Programming
- The Result asking one password
	```ascii
	Enter vault password: helo
	Exception in thread "main" java.lang.StringIndexOutOfBoundsException: begin 8, end 3, length 4
	at java.base/java.lang.String.checkBoundsBeginEnd(String.java:4604)
	at java.base/java.lang.String.substring(String.java:2707)
	at VaultDoorTraining.main(VaultDoorTraining.java:9)
	```
- No need to Run the code . Ok isit the content of java file.
- Because , The line number `24` Have password.
- I got flag after enter the password.



