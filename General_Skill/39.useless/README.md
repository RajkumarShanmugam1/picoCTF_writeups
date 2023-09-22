# useless

## Description
- There's an interesting script in the user's home directory.
- Author: LOIC SHEMA
- Tags  : picoCTF2021 , General skills
- Source: Live Instanse

<ins>Approach</ins> :
 First Start the instance using `Lanuch INstance`.
- Connect the server through `ssh`
  ```bash
  ssh -p <PORT> picoplayer@saturn.picoctf.net
  ```
  ![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/d34ba26f-47fd-42b4-90be-198696844f78)
- Here one file is there `useless`. Which ascii script file.
- Try to run that file. Which return `Read the file`
- Inside on ascii code.
  ```ascii
  #!/bin/bash
  # Basic mathematical operations via command-line arguments
  if [ $# != 3 ]
  then
    echo "Read the code first"
  else
    if [[ "$1" == "add" ]]
	    then 
	      sum=$(( $2 + $3 ))
	      echo "The Sum is: $sum"  
 	  elif [[ "$1" == "sub" ]]
	    then 
	      sub=$(( $2 - $3 ))
	      echo "The Substract is: $sub" 
	  elif [[ "$1" == "div" ]]
	    then 
	      div=$(( $2 / $3 ))
	      echo "The quotient is: $div" 
	  elif [[ "$1" == "mul" ]]
	    then
	      mul=$(( $2 * $3 ))
	      echo "The product is: $mul" 
	  else
	    echo "Read the manual"
	  fi
  fi
  ```
- In the else part read the manual
   ```bash
   man useless
   ```
- Here flag is there.
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/9cd7ea50-ad7c-4009-af5b-1b72903c95f1)
