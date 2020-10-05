# Reindeer Flotilla
```
It's time to enter the Grid. Figure out a way to pop an alert() to get your flag.
http://chal.ctf.b01lers.com:3006
Author: @MDirt
```

Accessing the page, we are greeted with with a "console" that basicly prints what we typed in. First thing I tried was obviously `<script>alert(1)</script>` but that did not execute the script as the HTML is only inserted into the page as text, not appended (create HTML node, append in document).

So the page does not trigger the javascript, how about we trigger it
```html
<img src="nope" onclick="alert(1)"/>
```
Then I clicked on that picture object and we get an alert! Then the flag is shown on the page.