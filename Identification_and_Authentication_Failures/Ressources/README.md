# Identification_and_Authentication_Failures

## Description

Confirmation of the user's identity, authentication, and session management is critical to protect against authentication-related attacks.

## Check_cookies

    First one, i see the website cookies keys: i_am_admin and a MD5 value: 68934a3e9455fa72420237eb05902327.
    68934a3e9455fa72420237eb05902327 -> after crack: flase
    So i just regenerate a "true" value in MD5: b326b5062b2f0e69046810717534cb09 and replace it.

## Get_flag

    After page refresh with the new cookies valus, i get a alert message that's a flag: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

