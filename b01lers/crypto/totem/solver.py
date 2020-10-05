#!/usr/bin/env python3

import socket
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'} 
  
def atbash(message): 
    cipherT = '' 
    for letter in message: 
        # checks for space 
        if(letter != ' '): 
            #adds the corresponding letter from the lookup_table 
            cipherT += lookup_table[letter] 
        else: 
            # adds space 
            cipherT += ' '
  
    return cipherT 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("chal.ctf.b01lers.com", 2008))

count = 0

while 1:
    data = s.recv(15)
    method = "NOTHING"
    cipher = "NOTHING"
    
    if data:
        if "Method" in repr(data):
            print("COUNTER ", count)
            method = repr(data).split()[1].split("\\n")[0].split("'")[0]
            print ("Method: ", method)
            
            data = s.recv(128)
            if "text" in repr(data):
                cipher = repr(data).split()[1].split("\\n")[0]
                print ("Cipher: ", cipher)
                
                decoded = "NOTHING"
                
                if method == "bacon":
                    decoded = os.popen("bacon -d --alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ' " + cipher).read().split()[0].lower()
                elif method == "Base64":
                    decoded = b64decode(cipher).decode("utf-8")
                elif method == "rot13":
                    decoded = codecs.decode(cipher, "rot_13")
                elif method == "atbash":
                    decoded = atbash(cipher.upper()).lower()
                
                print ("Decoded: " + decoded)
                decoded += '\n'
                s.send(decoded.encode())
                
                count += 1
                
                if count == 1000:
                    print(repr(s.recv(256)))
                    break

print ("Connection closed.")
s.close()