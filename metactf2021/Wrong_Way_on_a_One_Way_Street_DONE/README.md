# Wrong Way on a One Way Street

## Question
Hashing is a system by which information is encrypted such that it can never be decrypted... theoretically. Websites will often hash passwords so that if their passwords are ever leaked, bad actors won't actually learn the user's password; they'll just get an encrypted form of it. However, the same password will always hash to the same ciphertext, so if the attacker can guess your password, they can figure out the hash. Can you guess the password for this hash? `cb78e77e659c1648416cf5ac43fca4b65eeaefe1`

## Solve
Run johnny with the hash and use rockyou.txt wordlist.
We got the password: babyloka13
```
MetaCTF{babyloka13}
```