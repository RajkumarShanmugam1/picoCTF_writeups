# Cookies

## Description
- 

Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:21939/
- Author: syreal
- Tags  : picoCTF2021 , WebExploit
- Source: [URL](http://mercury.picoctf.net:21939/)

<ins>Step - 1</ins> :
- Checking out Burp Suite, one of it's main abilities it to intercept and modify requests. Burp Suite

Now by inspecting the webpage, we get something that looks like this

From here we see that the method that was used for Red was "GET" and for Blue was "POST". We can do more research on these, as they are different HTTP requests. Check out this webpage

It makes sense, as we figured earlier that Burp Suite can intercept and change requests. Looking through the list, we see that the second request method is "HEAD" which seems quite familiar. If we look back at the challenge title "Get aHead", the word Head stands out, probably referring to the HTTP Request method "HEAD".

There's different ways to approach this section, but we found downloading "Postman" as a chrome extension the easiest. Postman Chrome Extension

After opening up the app (it download as an app), choose the "request" option and create a folder. Feel free to name it whatever you like. From there, insert the website link into the "Enter request url" bar, change the method to "HEAD" and then click send. Now, don't forget to click into the "Headers" tab below, to find the flag! 
- tools : [ROT13](https://rot13.com/) , [CyberChef](https://gchq.github.io/CyberChef/)

