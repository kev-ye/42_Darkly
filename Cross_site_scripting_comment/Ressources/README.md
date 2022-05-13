# Cross_site_scripting

## Description

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

## Image_with_url_element

    At the index page, we have a image where we can click it.
    After click, we have a url with the params [page=media] and [src=nsa].
    So there, i try a XSS using Code Encoding: src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg.
    That i get a flag: 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d