	# autoYouLi(2)import os
import subprocess
import datetime
import time
from threading import Thread, Lock
import AutoDailyCounterpart1 as ADC
from AutoDailyCounterpart1 import AccountNumberException, Adventure
'''

该脚本专门用于刷三国志名将令的副本，要求为每天第一次打开游戏时执行（为了保证体力>50）

'''
deviceFlag = 2 # 1 - 01 , 2 - 25 , 3 - 27

NOList = ADC.NOList

NO = NOList[deviceFlag - 1]

presentAccountNumber = 0 # 当前切到了哪个号， 0 表示有问题

# @Global variable

# 记录每天已经完成任务的号
account_done_mission = ADC.autoInvokeList

# lvl no less than 70 # Email and friends diff
moreThan70 = ADC.moreThan70

# lvl no less than 65
autoInvokeList = ADC.autoInvokeList

# lvl no less than 58

def setNO(num):
	ADC.setNO(num)

def getNO():
	ADC.getNO()

# 记录每天已经完成任务的号
account_done_mission = ADC.account_done_mission

devices = 0 #devices = 0 # 0 - Mobile ; 1 - Simulator

isUsingScale = True
blank = " "
xscale = 1
yscale = 1 


if isUsingScale:
	scale = 600 / 1920

presentAccount = False

def connect(no = 26):
	ADC.connect(no)

def sleep(t):
	ADC.sleep(t)

def click(x, y):
	if devices == 2:
		os.system("adb -s 127.0.0.1:" + str(NO) + " shell input tap " + str(scale * x) + blank + str(scale * y + 57))
		# print("xclick:", scale * x, ", yclick:", scale * y + 57)
	else:
		raise Exception

def swipe(startx, starty, stopx, stopy):
	global devices
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input swipe " 
			+ str(startx) + blank + str(starty) + blank + str(stopx) + blank + str(stopy))
	if devices == 2:
		# print("adb -s 127.0.0.1:620" + str(NO) + " shell input swipe " + str(startx) + blank + str(starty) 
		# + blank + str(stopx) + blank + str(stopy))
		os.system("adb -s 127.0.0.1:" + str(NO) + " shell input swipe " + str(scale * startx) + blank 
			+ str(scale * starty + 57) + blank + str(scale * stopx) + blank + str(scale * stopy + 57))
'''
class AccountNumberException(Exception):
	"""docstring for AccountNumberException"""
	def __init__(self):
		super(AccountNumberException, self).__init__()
		print("presentAccountNumber should not be equal to ", presentAccountNumber)
'''
def back():
	click(105, 35)

def skipPlot():
	ADC.skipPlot()

def fight():
	ADC.fight()

def adbInput(string):
	if devices == 1:
		os.system("adb -s 127.0.0.1:62021 shell input " + string)
	if devices == 2:
		os.system("adb -s 127.0.0.1:" + str(NO) + " shell input " + string)

def switchAccount(x):
	ADC.switchAccount(x)

def autoDailyCounterpartRun():
	ADC.autoDailyCounterpartRun()

def autoDinner():
	ADC.autoDinner()

def autoMine():
	ADC.autoMine()

def choose_by_x_axis(x):
	ADC.choose_by_x_axis(x)

def chooseEnemy(x):
	ADC.chooseEnemy(x)

def enterBattle():
	ADC.enterBattle()

def autoNormalBattle():
	ADC.autoNormalBattle()

def autoMiddleBattle():
	ADC.autoMiddleBattle()

def autoClubSignIn():
	isBigAccount = presentAccount
	ADC.autoClubSignIn()

def autoShop():
	ADC.autoShop()

def countDays():
	ADC.countDays()

def countPositionXandY():
	ADC.countPositionXandY()

def autoFuli():
	ADC.autoFuli()

def autoGuo_guan_zhan_jiang():
	ADC.autoGuo_guan_zhan_jiang()

def autoDailyMission():
	ADC.autoDailyMission()

def autoArena():
	ADC.autoArena()

def autoLand():
	ADC.autoLand()

def autoDailyBonus():
	ADC.autoDailyBonus()

def autoCollectRedPiecesForOneTime():
	ADC.autoCollectRedPiecesForOneTime()

def yuandan():
	ADC.yuandan()

def autoCollectRedPieces():
	ADC.autoCollectRedPieces()

def autoInvoke(acc):
	ADC.autoInvoke(acc)

def autoCollectClubBonus():
	ADC.autoCollectClubBonus()

def autoCollectEmail():
	ADC.autoCollectEmail()

def autoFriends():
	ADC.autoFriends()

def autoFinishMission():
	ADC.autoFinishMission()

def autoYouLi(i):
	ADC.autoYouLi(i)
def run():
	print('run')
	# '''
	# 临时
	# switchAccount(7)
	for i in range(1, 4):
	# 	autoYouLi(2)
		autoNormalBattle()
	# '''


def main():
	print(deviceFlag)
	
	ADC.main(deviceFlag)
	
	# run()

if __name__ == '__main__':
	main()


