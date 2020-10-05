# Totem

```
Is this a dream or not? Use your totem to find out. Flag format: ctf{}.
nc chal.ctf.b01lers.com 2008
```
[totem-template.py](https://github.com/ducng99/ctf/blob/main/b01lers/crypto/totem/totem-template.py)

Now this is a pain in the ass.

Netcat to the server above, we are greet with questions asking us to decrypt or decode the given cipher. Reading the template they gave, the server have 4 types of encrypt/encode: bacon, base64, atbash and rot13. A quick search will give us a basic how-to solve these. Another thing to note is
```py
if count == 1000:
    print(r.recv())
```
Yeah, we need to solve 1000 questions. But of course we programmers (I hope).

So I have made this cheesy python script to parse method and ciphertext then solve them and send back to the server 1000 times, then read the final message, which is our flag

--> [solver.py](https://github.com/ducng99/ctf/blob/main/b01lers/crypto/totem/solver.py)