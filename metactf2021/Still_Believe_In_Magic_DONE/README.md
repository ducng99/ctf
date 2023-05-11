# Still Believe in Magic

## Question
We found an archive with a file in it, but there was no file extension so we're not sure what it is. Can you figure out what kind of file it is and then open it?

## Solve
Use `tar -xzvf magic.tar.gz` to extract the file. Looking at the file `magic` in hex, the first 2 letters `PK` means the file is a zip file.

Unzip the file with `unzip magic` and we get `magic.txt` file, which has the flag
```
MetaCTF{was_it_a_magic_trick_or_magic_bytes?}
```