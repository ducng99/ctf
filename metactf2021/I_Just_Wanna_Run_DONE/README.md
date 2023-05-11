# I Just Wanna Run

## Question
Our security team has identified evidence of ransomware deployment staging in the network. We’re trying to contain and remediate the malicious operator’s deployment staging and access before the operator successfully spreads and executes ransomware within the environment. We’ve recovered some of the operator’s staging scripts and files. Can you help identify which user account’s credentials the operator had compromised and is planning to use to execute the ransomware?

## Solve
Unzip the file and we got a list of recovered files. Looking at `exe.bat` file, we can see an user is being used `METAL\timq-admin`