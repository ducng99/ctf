# NahamCon 2021 Write-ups
## Beginning tasks
These tasks are "hidden" website HTML source code or in Discord channel description. They are easy to find.
- Read the rules
- #NahamCon2021
- UHC-BR
- Red Team Village
- Merch Store
- Live Recon Village
- IoT Village
- INE Career Corner
- HTB Village

## esab64
It's litterally base64 reverse string
The given string in file provided is
```
mxWYntnZiVjMxEjY0kDOhZWZ4cjYxIGZwQmY2ATMxEzNlFjNl13X
```
Reversing that we get
```
X31lNjFlNzExMTA2YmQwZGIxYjc4ZWZhODk0YjExMjViZntnYWxm
```
Do a base64 decode and we get the flag in reverse
```
_}e61e711106bd0db1b78efa894b1125bf{galf
Poof: flag{fb5211b498afe87b1bd0db601117e16e}
```

## 