# Permissions

## Description
- Can you read files in the root file?
Additional details will be available after launching your challenge instance.
- Author: GEOFFREY NJOGU
- Tags  : picoCTF2021 , General skills
- Source: `Live Instance`

<ins>Approach</ins> :
- First Start the instance using `Lanuch INstance`.
- Connect the server through `ssh`
  ```bash
  ssh -p <PORT> picoplayer@saturn.picoctf.net
  ```
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/6ba5e47f-97a4-4afb-86c9-6c600565487f)
- Here challenge permission is denied for all users.
- Check the previleged commands in
  ```bash
  sudo -l
  ```
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/fa7443fb-de71-42b6-8389-68d4898967b4)
- Here vi command is give the access like as `sudo`. Here easily run all commands.
- enter the command:
  ```bash
  sudo vi
  ```
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/d52f46ba-3fd6-4711-9453-3343b237b86f)
- Enter need commands in command mode of vi.
  ```
  ls /challenge
  ```
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/55e1da4c-0323-4cda-9006-da7fa999ad36)

![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/d41a2998-9ccd-4cd8-a7b5-f62c46208bb6)
- Here easily got inside file details of folder `challenge`
- Show the metadata.json file
```bash
! cat /challenge/metadata.json
```
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/9df5a266-8a94-48a4-bb5b-e812bb444da8)

![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/f52d81a7-6c67-40d9-9f01-90663956c293)
 - Here i used the to show the metadata
 - But shown need on `/root/flag.txt`
