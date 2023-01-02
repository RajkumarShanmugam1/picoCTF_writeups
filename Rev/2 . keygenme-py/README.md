# keygenme-py

## Description
- [keygenme-trial.py](./keygenme-trial.py)
- Author: syreal
- Tags  : picoCTF2021 , Cryptography
- Source: [keygenme-trial.py](./keygenme-trial.py)

<ins>Approach</ins> :
- The python have a details of decryption.
- The user name trial is given in the pgm .
```text
username_trial = "GOUGH"
bUsername_trial = b"GOUGH"
```
- After the few lines have the template of key
```text
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
- star ,  intro_trial() ,... , enter_license() are not needed.
- In `check_key(key, username_trial)` the check function have details of key
```text
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False
```
- The hexdigest in order of `[4,5,3,6,2,7,1,8]` which is digest and add cender part of key
- So the [solve.py](./solve.py) have the solution program.
- The flag is got after run the `solve.py`
