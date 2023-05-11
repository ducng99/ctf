# Sharing Files and Passwords

## Questions
FTP servers are made to share files, but if its communications are not encrypted, it might be sharing passwords as well. The password in this pcap to get the flag

## Solve
Open the file with wireshark and find a packet has `PASS` and following is the password `ftp_is_better_than_dropbox`