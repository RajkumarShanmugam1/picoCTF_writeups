# repetitions

## Description
- Can you make sense of this file?
Download the file [here](./enc_flag).
- Author: GEOFFREY NJOGU
- Tags  : picoCTF2021 , General skills
- Source: [enc_flag](./enc_flag)

<ins>Approach</ins> :
- In the file one encode or hash is there.
  ```ascii
  VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVhRm
  RXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
  MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
  VkpEVGxaYVdFMVhSbFZhTTBKUFdXdGtlbVF4V2tkWGJYUllDbUY2UWpSWmEyaFRWakpHZEdWRlZs
  aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
  ```
- In the end of the encode `==` , Which is looks like `base64`
- So tried to decode using [CyberChef](https://gchq.github.io/CyberChef/)
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/bae77bd9-e73d-4d4f-b0f4-b35452b9cd1c)
- Use multible time of `base64` in [CyberChef](https://gchq.github.io/CyberChef/)
![image](https://github.com/RajkumarShanmugam1/picoCTF_writeups/assets/76644058/5d6d48be-f530-415d-8e2c-f631b0549de3)
- Finally got the flag.
