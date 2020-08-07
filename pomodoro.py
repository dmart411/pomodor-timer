import datetime as dt
import time
import webbrowser
import random
import math
import requests
import os
from songsyt import songs

'''
MODE 1 OPENS A YOUTUBE VIDEO OF A SONG, MODE 2 PLAYS A SUCCESION OF BEEPS
'''
def alarm(mode):
	if mode == 1:
		title, link = random.choice(list(songs.items()))
		res = requests.get(link)
		res.raise_for_status()
		print('YOUR TIMER ENDED!! OPENING "' + title + '" ON YOUTUBE...')
		webbrowser.open(link)
	elif mode == 2:
		print('\a\a\a\a\a')
'''
SETS A TIMER FOR NUMBER OF MINUTES SPECIFIED IN THE PARAMATER VAR
'''
def setTimer(length): # takes arguments as minutes
	dtnow = dt.datetime.now()
	dfinal = dtnow + dt.timedelta(minutes=length)
	while True:
		dtnow  = dt.datetime.now()
		if dtnow >= dfinal:
			break
		delta = dfinal - dtnow 
		print('TIME LEFT: ' + str(math.trunc(delta.total_seconds()/60))+' MINUTES '+str(round(delta.total_seconds()%60)) + ' SECONDS')
		time.sleep(1)
'''
POMODORO TIMER LOGIC. GIVES USER CHOICE BETWEEN CLASSIC MODE OR CUSTOM MODE,
GIVES USER CHOICE BETWEEN SHORT OR LONG BREAK
'''
def pomodoro():
	while True:
		start = input('START POMODORO!\nENTER "1" FOR CLASSIC(25 MINUTES) OR "2" FOR CUSTOM: ')	
		if start == '1':
			setTimer(25)
			break
		if start == '2': 
			length = input("ENTER LENGTH OF POMODORO (IN MINUTES) BETWEEN 1 AND 60: ")
			while True:
				if length.isdigit() and int(length) >= 1 and int(length) <= 60: 
					break
				print('INVALID LENGTH')
			setTimer(int(length))
			break
		else:
			print('INVALID OPTION. TRY AGAIN.')				
	alarm(1)
	while True:	
		start = input('START BREAK!\nENTER "1" FOR 5 MINUTES "2" FOR 15 MINUTES: ')
		if start == '1':
			setTimer(5)
			break
		if start == '2':
			setTimer(15)
			break
		else:
			print('INVALID OPTION. TRY AGAIN.')
	alarm(2)

'''
MAIN FUNCTION. LOOPS TO ALLOW FOR MULTIPLE POMODORO TIMERS IN ONE SESSION
KEEPS COUNT OF TIMERS COMPLETED AND DISPLAYS TO USER 
'''
def main():
	count = 0
	pomodoro()
	count += 1
	print('POMODORO ENDED!! TOTAL POMODOROS - ' +str(count))
	cont = input('START AGAIN? (Y/N): ')
	while True:
		if cont.upper() == 'Y':
			pomodoro()
			count += 1
			print('POMODORO ENDED!! TOTAL POMODOROS - ' +str(count))
		elif cont.upper() == 'N':
			break
		else:
			print('INVALID OPTION. TRY AGAIN')

if __name__ == "__main__":
    main()
