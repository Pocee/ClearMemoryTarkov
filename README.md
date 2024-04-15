Disclaimer!!!
This only will work if your configure Task Scheduler manually, will we detailed below.

Contains:

EmptyStandbyList.exe: (https://web.archive.org/web/20220606204216/https://wj32.org/wp/software/empty-standby-list/)
Program made by wj32, site is down that's why i'm using archive.org. You can download from there if you doesn't want to take risks using mine.
This program just clear all StandBy memory from Windows this can be checked on Windows Resource Monitor.

Checker.py: simple program made by myself, just checks that escape from tarkov is open and then if it is open clear memory every 200 seconds, you can easily modify to any time you want or if you want this program to any another app or game.

opener.bat: just opens "checker.py" that will be linked on Task Scheduler.


CONFIGURATION:
1.- Open Task Scheduler. WindowsKey + R --> taskschd.msc
2.- Create a new task (located on right side) 
3.- Every window config.
General: click on second circle (run whether the user is logged in or not) and DO NOT STORE PASSWORD check, run with the highest privileges. And configure for W10
Triggers: new --> Start task when logging in
Actions: Link checker.py on program/script section and accept.

You can check if it works right clicking on task name and clicking on execute. Should show (executing) and Resource Monitor memory Standby should be gone. 
This script will be always active and should clean memory every 200 seconds, this remember can be changed on .py file.
That's all 

