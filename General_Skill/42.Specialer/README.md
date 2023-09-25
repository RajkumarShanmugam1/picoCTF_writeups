# Specialer
## Description
- Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.
Additional details will be available after launching your challenge instance.
- Author: LT 'SYREAL' JONES
- Tags  : picoCTF2021 , General skills
- Source: Live Instance

<ins>Approach</ins> :
- The give source is Hexadecimal.
- First Start the instance using Lanuch INstance.
- Connect the server through ssh
  ```
  ssh -p <PORT> picoplayer@saturn.picoctf.net
  ```
- Here some command are supported by bash. Some command are not support.
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/d624b856-acb4-4b62-8f05-1b4b0eadb740)
- `compgen -c` is used to shown supported commands.

   ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/7f763b34-6eb1-4077-949f-009facc3b668)
- `cd <tab> <tab>`. cd + double TAB is used to shown the available . Which is easily traverce the directory.
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/b1653da4-45f2-456f-a238-6a3bc0a46cbe)
- Display the content file using `echo "$(<FILE-NAME)"`.
- Explore all directory.
  
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/09d39acb-54da-4c3c-92b2-f1e9bae03e5a)
