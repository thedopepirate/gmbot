HELLO THERE ! THIS BOT JOINS Google Meet AUTOMATICALLY BY IMAGE RECOGNITION AT SCHEDULED TIME WITH THE LINK, IF THERE ARE LESS THAN 10 PEOPLE IN THE MEETING, IT WILL QUIT THAT MEETING AND JOIN THE NEXT MEETING.
IT ALSO MUTES YOUR MIC AND DISABLES VIDEO BEFORE ENTERING THE MEETING.

ONLY WORKS ON CHROME BROWSER!!!! THE CHROME BROWSER MUST NOT HAVE DARK THEME !!!!! SET IT TO DEFAULT THEME!!!!

**STEP ONE**

CHECK IF YOUR PC IS 64-BIT OR 32-BIT FIRST BY GOING TO "THIS PC or My Computer" and right click -> properties

you can see it there. ( if your system shows 64-bit processor, 32-bit OS then you need to install 32-bit softwares)
 

INSTALL GIT BASH (download the setup file and just keep clicking yes till the installation finishes)

(Download link)

https://git-scm.com/download/win (DOWNLOAD 32bit or 64 bit depending upon your pc)

After the installation is done :---

Clone my repository by opening git bash FROM START MENU (follow the instructions given below)

YOU CAN OPEN GIT BASH BY GOING TO START MENU AND TYPING GIT BASH, CLICK ON IT, THEN TYPE

```cd Desktop```

PRESS ENTER

COPY AND PASTE THE CODE BELOW

```git clone https://github.com/thedopepirate/gmbot.git```

PRESS ENTER

THE FOLDER NAMED 'gmbot' MUST BE DOWNLOADED IN YOUR DESKTOP NOW

COPY THIS FOLDER TO YOUR C DRIVE AND PASTE IT



CLONE THE BELOW REPOSITORY NOW, BY OPENING GIT BASH FROM START MENU AND TYPE:

```cd Desktop```

press enter, and now type

```git clone https://github.com/thedopepirate/extensiongmeet.git```

press enter.

A FOLDER NAMED ```extensiongmeet``` MUST BE ON YOR DESKTOP NOW.

COPY THAT FOLDER AND PASTE IT IN C DRIVE

OPEN CHROME

FOLLOW THESE INSTRUCTIONS

<div align="center">
<img src="https://github.com/thedopepirate/extensiongmeet/blob/main/INSTALLEXTENSION/step1.png" >
<p>CLICK ON EXTENSIONS</p>
</div>

<div align="center">
<img src="https://github.com/thedopepirate/extensiongmeet/blob/main/INSTALLEXTENSION/step2.png" >
<p>ENABLE DEVELOPER MODE AND THEN CLICK ON LOAD UNPACKED</p>
</div>

<div align="center">
<img src="https://github.com/thedopepirate/extensiongmeet/blob/main/step3.png" >
<p>GO TO C DRIVE WHERE YOU PASTED THE ```extensiongmeet``` FOLDER, SELECT IT</p>
</div>

<div align="center">
<img src="https://github.com/thedopepirate/extensiongmeet/blob/main/INSTALLEXTENSION/step4.png" >
<p>GO TO THE EXTENSION SHORTCUT AND PIN IT</p>
</div>

<div align="center">
<img src="https://github.com/thedopepirate/extensiongmeet/blob/main/step5.png" >
<p>IT SHOULD LOOK LIKE THIS</p>
</div>


**STEP 2**

INSTALL PYTHON ON YOUR PC

WATCH THE VIDEO ATTACHED BELOW FOR INSTALLATION AFTER DOWNLOAD (important)

DOWNLOAD LINKS:------

FOR WINDOWS 10 OR 8

https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe (FOR 32-BIT OS)

https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe (64-BIT)

IF YOU ARE USING WINDOWS 7, THEN install

https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi (32 bit)

https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi (64 BIT)


***WATCH THIS VIDEO ON HOW TO INSTALL PYTHON AFTER DOWNLOADING THE ABOVE SETUP (Very IMPORTANT)***

https://youtu.be/DKXMUGuGMp4

THE ABOVE SETUP (Very IMPORTANT) https://youtu.be/DKXMUGuGMp4

**STEP 3**

WE NEED PIP INSTALLED(follow this tutorial)

https://youtu.be/7Qxn4gcrGwg

GO TO THIS LINK, RIGHT CLICK AND SAVE IT ON DESKTOP.

https://bootstrap.pypa.io/get-pip.py

ONCE THAT IS DONE, CLICK IT OPEN ( YOU NEED TO INSTALL PYTHON BEFORE DOING THIS)

AND THAT WILL INSTALL PIP

AFTER YOU INSTALL PIP, OPEN GIT BASH FROM START MENU AND TYPE

```pip -V```

CLICK ENTER

THE OUTPUT SHOULD LOOK SOMETHING LIKE THIS (not exact though)

```pip 20.2.3 from c:\program files\lib\site-packages\pip (python 3.9)```

**SKIP TO STEP 4 IF YOU SEE A SIMILAR OUTPUT**


***ERROR HANDLING*** 


***IF THERE IS AN ERROR, LIKE bash: pip: command not found THEN DO WATCH THIS VIDEO. (skip if the above output is seen)***

-> https://youtu.be/yNJl2t5xPck


GO TO THE FOLDER WHERE PYTHON IS INSTALLED AND OPEN THE FOLDER NAMED SCRIPTS (IF YOU FOLLOWED THE PYTHON INSTALLATION VIDEO, THIS WOULD BE THE LOCATION)

```C:\Program Files\Scripts```

NOW CLICK ON START MENU AND TYPE

```sysdm.cpl ```

OPEN the application

Go to the Advanced tab, then click on Environment Variables

In the POPUP, UNDER SYSRTEM VARIABLES COLUMN, click on "Path" to select it. Then with the Path selected, click the Edit… button.

In the Edit environment variable screen, click on New and add the path where the PiP installation is located ```C:\Program Files\Scripts``` click ok

OPEN GIT BASH AND TYPE

```pip -V```
it should be working now


**STEP 4**

INSTALL pyautogui , datetime and pandas

GO TO GIT BASH

TYPE AND PRESS ENTER

```pip install pyautogui```

AFTER THE INSTALLATION IS DONE TYPE FOLLOWED BY ENTER KEY

```pip install pandas```

AFTER THE INSTALLATION IS DONE TYPE FOLLOWED BY ENTER KEY

```pip install datetime```

AFTER THE INSTALLATION IS DONE TYPE FOLLOWED BY ENTER KEY

```pip install Pillow```

AFTER THE INSTALLATION IS DONE TYPE FOLLOWED BY ENTER KEY

```pip install opencv-python```


**STEP 5**

GO TO THE FOLDER NAMED 'gmbot' IN YOUR C DRIVE, OPEN THE FILE

OPEN THE FILE enter.csv IN NOTEPAD

YOU NEED TO ENTER THE MEETING DETAILS LIKE I HAVE SHOWN YOU IN THE THREE EXAMPLES IN FILE enter.csv

FORMAT (date/month/year hour:minute:seconds) 24 hrs format

***use comma to seperate the time and links !!!!!! do not leave spaces!!!***

YOU WILL HAVE TO CHANGE THE LINKS AS PER YOUR SCHEDULE

SAVE IT

**MAIN STEP**

DOUBLE CLICK ON THE FILE main.py

JUST WAIT AND RELAX, MY BOT WILL AUTOMATICALLY JOIN THE MEETING (enter the timings and LINKS correcrly in enter.csv)

YOU NEED TO OPEN THE FILE main.py ATLEAST A MINUTE BEFORE THE time you entered in ```enter.csv``` file to join the meeting.

once the meeting ends, it will join the next meeting AUTOMATICALLY by reading the time in enter.csv

the commands might take some time, do not move your mouse or type when running the bot.

IF YOU WISH TO YOU CAN FURTHER AUTOMATE THE BOT BY TASK SCHEDULING SO THAT IT RUNS main.py AUTOMATICALLY using task scheduler.

watch this video

THANKS FOR DOWNLOADING MY BOT

Follow me on insta @thedarknlucid

wubba lubba dub dub
