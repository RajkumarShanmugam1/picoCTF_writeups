# chrono

## Description
- How to automate tasks to run at intervals on linux servers?
Additional details will be available after launching your challenge instance.
- Author: MUBARAK MIKAIL
- Tags  : picoCTF2021 , General skills
- Source: `Live Instance`

<ins>Approach</ins> :
- First Start the instance using `Lanuch Instance`.
- Connect the server through `ssh`
	- ssh <USER>@saturn.picoctf.net -p <PORT>
 	- After Connect :
 ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/fbafdace-ceec-444f-b2bd-458382eae65f)
- Which task is related to automation.
- Automation are achived by crontabs and cronjobs in Linux.
- Check the crontabs in the location `/etc/crontab`.
  ```bash
  cat /etc/crontab
  ```
- Finally automation is finish with proof of flag in the location `/etc/crontab`.
