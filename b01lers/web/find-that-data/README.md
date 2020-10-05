# Find that data

```
Complete what Clu could not... Find the data in memory. https://www.youtube.com/watch?v=PQwKV7lCzEI
http://chal.ctf.b01lers.com:3001
```

Open the site, we are prompted to login. Viewing the source code and we got
```js
function login(username, password) {
    if (username == "CLU" && password == "0222") {
        window.location = "/maze";
    } else window.location = "/";
}
```
With `CLU` and `0222` we logged into the site and greeted with a auto-generated maze.
Obviously we won't be playing the maze (I did after finishing tho, we won't be able to finish it as the final node is always blocked, pfft scammers)

Viewing the source code to look for additional hints, we found `maze.js`, opened and examine the file, we found a function send POST request to `/token` and `/mem`. The function that send to `/mem` already reads `#token` element so we don't need to care about that, calling the POST function in browser console gave us an alert with the flag.
```js
$.post("/mem", { token: $("#token").html() }).done(function(data) {
    alert("Memory: " + data);
});
```