# Special
## Description
- Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
Start your instance to see connection details.
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
- All command input are changed and implement. Here `ls` converted as `Is`
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/aeaef804-eb9d-4bf5-a28b-bcb711e1da91)
- So try to inmplement in the special character. Because which is special task.
- First try to `"COMMAND"`, `"ls"` -> also , `"pwd"` -> worked
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/175cc2bf-6197-4515-8e87-c10531adf867) 
- Here `grep` is worked but `grep --help` doesnot worked.
- Because `--` is also special. use as out side `"grep" --"help"`.
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/9934839b-65a5-4374-9905-cedda8d4f284)
- `--recursive` is used to shown recursively worked the grep.
- Use the recursive to show all. `"grep" --"recursive"`
- But which is not work. Because there was no termination.
- `"grep" --"recursive" .` , `.` is used in the end.
