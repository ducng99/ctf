# Log

```
GET the right file.
http://3.7.251.179/
```

The description has a hint GET, we need to find a file, I can't be more obvious, a log file.

Opening the site, we are greeted with 99 links to 99 pages, as what I usually do, I viewed the source code and found there is a link that is not in order with others

![1](https://i.imgur.com/2TwEO06.png)

Accessing the page, we are greeted with `You got the right 'file' :) `. The hint here is file, and we need to `GET` a log. The vulnerability here is at `http://3.7.251.179/click-here_00.php?file=<PATH>`. Using local file inclusion I can read logs on the server, outside the /var/www/html scope.

After a long research and some trials and errors, I finally found `/var/log/apache2/error.log` -> `http://3.7.251.179/click-here_00.php?file=/var/log/apache2/error.log`. Looks like a lot of people were there too lol. So the job here is to write content into this log file, but this isn't access.log where you can simply access the page and get a line in the log, it only writes when PHP returns an ERROR, not even WARNING. And our inclusion is using `include()` command, which does not show ERROR if the file is not found, only `require()` will return an ERROR. So I researched a bit more on how to trigger an error, I stumbled on .htaccess file, this file is forbidden for users so whenever someone access `http://3.7.251.179/.htaccess`, it will pop an ERROR with name of the file.

![2](https://i.imgur.com/TKrmNZv.png)

So with .htaccess file, we can put our PHP script in and start digging this server up!

To begin, when you enter a non URL-encoded string such as `http://3.7.251.179/.htaccess<?php ?>`, the site will interpret `?` as parameter start section, therefore our ERROR message will not include the part from the question mark (`php ?>`), this applies for `?`, `/`, `\`

![3](https://i.imgur.com/fWlgHwi.png)

So we need to encode our PHP script before passing it over. Because we don't know where the flag is on the system, the best bet would be to list all files in the system.

*The process of making and tweaking the script takes a while, so I'll just skip and say "Here it is"*

```php
#Original
<?php echo "<pre>"; var_dump(exec("find ".DIRECTORY_SEPARATOR)); echo "<".DIRECTORY_SEPARATOR."pre>"; ?>
#Encoded
<%3Fphp echo "<pre>"%3B var_dump(exec("find ".DIRECTORY_SEPARATOR))%3B echo "<".DIRECTORY_SEPARATOR."pre>"%3B %3F>
```

`DIRECTORY_SEPARATOR` is there to replace `/` in `</pre>`. `<pre>` tag would help us displaying the output in lines with spaces, much easier to work with

The script would dump list of all files in all directories that it can access into `error.log`

It will show like 1000 lines or something like that but at the bottom, we can see a file nested in multiple folders: `/f/l/a/g/somethingUneed.txt`

Using the file inclusion above, we can read the flag `http://3.7.251.179/click-here_00.php?file=/f/l/a/g/somethingUneed.txt`

<details>
<summary>FLAG (spoiler)</summary>
BSDCTF{L0cal_f1L3_InClu$10N_1$_v3RY_P015On0u$}
</details>