# Robot Master

Check `/robots.txt`, I found `/cookie.php`. Because of the file name, I checked my cookies and found `Our_Fav_Cookie` and `Piece` has been set.

`Our_Fav_Cookie` looks like SHA256 and `Piece` is a number that keeps adding 1 everytime we access the cookie.php page.

I wrote a simple script to collect all hashes after found out there are maximum 39 pieces (`Piece` returns to 1 when exceed its maximum)

```py
import requests

with requests.Session() as s:
    for i in range(1, 40):
        r = s.get("http://15.206.202.26/cookie.php")
        print(s.cookies.get("Our_Fav_Cookie"))
```

After that I put every hashes on CrackStation and found the result `OFQPGS{P00x135_ne3_o35g_cy4p3_70_pu3px}`
Of course our flag should start with `BSDCTF{`, this is a ciphered text. And tested with Ceasar to decode with offset/key 13, we have the result:

`BSDCTF{C00k135_ar3_b35t_pl4c3_70_ch3ck}`