# Bases

## Description
- What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.
- Author: Sanjay C/Danny Tunitis
- Tags  : picoCTF2021 , General skills
- Source: `bDNhcm5fdGgzX3IwcDM1`

<ins>Approach</ins> :
- source is `bDNhcm5fdGgzX3IwcDM1` . I think this is the base encoded string.
- So decode the string using base decode.
- Convert the base64 value to normal text.

- command:
    ```sh
    echo "bDNhcm5fdGgzX3IwcDM1" | base64 --decode
    ```
    - `echo` is used display content in Linux mode .
    - `base64` is used to encode and decode the message / content .
    
- ( OR )
- But this is `bDNhcm5fdGgzX3IwcDM1` using [RapidTales](https://www.base64decode.org/) to NOrmal text .

- Finally i got the flag `picoCTF{Your_Ouput}`
