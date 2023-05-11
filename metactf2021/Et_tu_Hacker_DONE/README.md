# Et tu, Hacker?

## Question
The law firm of William, Ian, Laura, and Lenny (WILL for short) has just been the victim of an attempted cyber attack. Someone tried to brute force the login for one of their employees. They have the event logs of the incident, and were wondering if you could tell them which user was targeted.

## Solve
Open the file in Event Viewer on a Windows machine, we can see a list of `Logon` events. They all have
```xml
<Data Name="TargetUserName">ericm</Data> 
```
The flag is
```
MetaCTF{ericm}
```