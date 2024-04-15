<p class="has-line-data" data-line-start="0" data-line-end="2">Disclaimer!!!<br>
This only will work if your configure Task Scheduler manually, will we detailed below.</p>
<p class="has-line-data" data-line-start="3" data-line-end="4">Contains:</p>
<p class="has-line-data" data-line-start="5" data-line-end="8">EmptyStandbyList.exe: (<a href="https://web.archive.org/web/20220606204216/https://wj32.org/wp/software/empty-standby-list/">https://web.archive.org/web/20220606204216/https://wj32.org/wp/software/empty-standby-list/</a>)<br>
Program made by wj32, site is down that’s why i’m using <a href="http://archive.org">archive.org</a>. You can download from there if you doesn’t want to take risks using mine.<br>
This program just clear all StandBy memory from Windows this can be checked on Windows Resource Monitor.</p>
<p class="has-line-data" data-line-start="9" data-line-end="10">Checker.py: simple program made by myself, just checks that escape from tarkov is open and then if it is open clear memory every 200 seconds, you can easily modify to any time you want or if you want this program to any another app or game.</p>
<p class="has-line-data" data-line-start="11" data-line-end="12">opener.bat: just opens &quot;checker.py</a>&quot; that will be linked on Task Scheduler.</p><br>
<p class="has-line-data" data-line-start="14" data-line-end="21">CONFIGURATION:<br>
1.- Open Task Scheduler. WindowsKey + R --&gt; taskschd.msc<br>
2.- Create a new task (located on right side)<br>
3.- Every window config.<br>
General: click on second circle (run whether the user is logged in or not) and DO NOT STORE PASSWORD check, run with the highest privileges. And configure for W10<br>
Triggers: new --&gt; Start task when logging in<br>
Actions: Link checker.py on program/script section and accept.</p>
<p class="has-line-data" data-line-start="22" data-line-end="25">You can check if it works right clicking on task name and clicking on execute. Should show (executing) and Resource Monitor memory Standby should be gone.<br>
This script will be always active and should clean memory every 200 seconds, this remember can be changed on .py file.<br>
That’s all</p>
