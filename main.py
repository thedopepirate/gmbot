import subprocess
import pyautogui
from time import sleep
import pandas as pd
from datetime import datetime
import webbrowser
def sign_in(link):
	#opens the link
	print("inside")
	webbrowser.open(link, new=20)
	print("opening")
	sleep(15)

	#mutes and turns off video
	sleep(10)
	while pyautogui.locateOnScreen('C:\gmbot\joinss.png'):
		if pyautogui.locateOnScreen('C:\gmbot\joinss.png'):
			sleep(2)
			pyautogui.hotkey('ctrl', 'd')
			pyautogui.hotkey('ctrl', 'e')
			print("muted and cam off")
			break
		else: print(".")
	sleep(2)
	while pyautogui.locateOnScreen('C:\gmbot\joinn.png'):
		if pyautogui.locateOnScreen('C:\gmbot\joinn.png'):
			sleep(2)
			pyautogui.hotkey('ctrl', 'd')
			pyautogui.hotkey('ctrl', 'e')
			print("muted and cam off")
			break
		else: print(".")
	sleep(2)
	#clicks join
	print("clicking the join button")
	while pyautogui.locateOnScreen('C:\gmbot\joinss.png'):
		if pyautogui.locateOnScreen('C:\gmbot\joinss.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('C:\gmbot\joinss.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("clicked on join")
			break
		else: print("")
	while pyautogui.locateOnScreen('C:\gmbot\joinn.png'):
		if pyautogui.locateOnScreen('C:\gmbot\joinn.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('C:\gmbot\joinn.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("clicked on join")
			break
		else: print("")
	# if there is a prompt for recording
	while  pyautogui.locateOnScreen('C:\gmbot\joinss.png'):
		if pyautogui.locateOnScreen('C:\gmbot\joinss.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('C:\gmbot\joinss.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("recording granted")
			break
		else: print(".")

	while  pyautogui.locateOnScreen('C:\gmbot\joinn.png'):
		if pyautogui.locateOnScreen('C:\gmbot\joinnn.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('C:\gmbot\joinn.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("recording granted")
			break
		else: print(".")
	sleep(1800)
	#leaves the meeting automatically if attendees are below 10 (CHECKS EVERY 5 MINUTES AFTER THE FIRST 30 MINUTES)
	while pyautogui.locateOnScreen('C:\gmbot\endd.png'):
		for i in range (0,9):
			sleep(300)
			print("entered for",i)
			if pyautogui.locateOnScreen('C:\gmbot\endd.png'):
				if pyautogui.locateOnScreen('C:\gmbot\whtext.png'):
					sleep(2)
					j = pyautogui.locateOnScreen('C:\gmbot\whtext.png')
					pyautogui.click(j)
					sleep(1)
					pyautogui.click(j)
					pyautogui.moveTo(x=698, y=385)
					break
					break
					print("MEETING LEFT, WAIT FOR NEXT MEETING")
				else: print("no")

	
print("I'm Looking for the timetable")
print("please wait......")
df = pd.read_csv('C:\gmbot\enter.csv')

while True:
	#checking timetable
	now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	if now in str(df['timings']):
		row = df.loc[df['timings'] == now]
		link = str(row.iloc[0,1])
		print(link)
		sign_in(link)
		sleep(5)
		print("LOOKING FOR THE NEXT ONE")
