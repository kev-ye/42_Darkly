# Cross_site_scripting

# Description

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

# Error_about_code_logic

    When i trying let some comment on feedback form, that console show me some error message about form:
    "checkForm is not defined" and "mtxMessage is not defined".

    - checkForm is a event function bind to button "SIGN GUESTBOOK"
    - mtxMessage is a comment value

    So that's i think here, we can try some xss attack.

# Insert_script_to_input_and_get_flag

    I tried some comment with "<script>" tag on "Message" and some a "<" character on "Name".
    And finally i get The flag: 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e