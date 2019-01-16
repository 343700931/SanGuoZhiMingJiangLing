import os
import subprocess
import datetime
import time
from threading import Thread, Lock
import AutoDailyCounterpart1 as ADC
from AutoDailyCounterpart1 import AccountNumberException, Adventure
'''

该脚本专门用于刷三国志名将令的副本，要求为每天第一次打开游戏时执行（为了保证体力>50）

'''
deviceFlag = 3 # 1 - 01 , 2 - 25 , 3 - 27

NOList = ["01", "25", "27"]

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
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input tap " + str(x) + blank + str(y))
	if devices == 2:
		os.system("adb -s 127.0.0.1:620" + str(NO) + " shell input tap " + str(scale * x) + blank + str(scale * y + 57))
		# print("xclick:", scale * x, ", yclick:", scale * y + 57)

def swipe(startx, starty, stopx, stopy):
	global devices
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input swipe " 
			+ str(startx) + blank + str(starty) + blank + str(stopx) + blank + str(stopy))
	if devices == 2:
		# print("adb -s 127.0.0.1:620" + str(NO) + " shell input swipe " + str(startx) + blank + str(starty) 
		# + blank + str(stopx) + blank + str(stopy))
		os.system("adb -s 127.0.0.1:620" + str(NO) + " shell input swipe " + str(scale * startx) + blank 
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
		os.system("adb -s 127.0.0.1:620" + str(NO) + " shell input " + string)

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
'''
class Adventure(object):
	"""docstring for Adventure"""
	def __init__(self):
		super(Adventure, self).__init__()
		def enterAdventure(self):
			print("现在进入冒险")
			click(1591, 990)
			sleep(4)
		enterAdventure(self)

	def enter1Arena(self):
		# 竞技场
		click(247, 515)
		sleep(2)

	def enter2DailyMission(self):
		# 日常副本
		click(785, 515)
		sleep(2)

	def enter3Guo_guan_zhan_jiang(self):
		# 过关斩将
		click(1316, 515)
		sleep(2)

	def enter4Land(self):
		# 领地巡逻
		click(1820, 515)
		sleep(2)

	def applyAuto1Arena(self):
		self.enter1Arena()
		# 只自动刷5次，无论成败
		click(1662, 883)
		sleep(0.2)
		click(1662, 883)
		sleep(0.2)
		sleep(2)

		back()
		sleep(3)

	def applyAuto2DailyMission(self):
		self.enter2DailyMission()
		# 分日期, 1、3、5、7 已确定
		if int(time.strftime("%w")) in [1, 3, 5, 0]:
			# 突破丹、宝物精炼石、装备精炼石
			self.breakthrough()

			self.treasureRefiningStone()

			self.weaponRefiningStone()

		if int(time.strftime("%w")) in [2, 4, 6, 0]:
			# 武将经验、宝物经验、神兵进阶
			self.heroExp()

			self.treasureExp()

			self.spiritWeaponLvlupStone()
			
		self.gold()

		print("DailyMission END")
		back()
		sleep(3)

	# 1.3.5.7
	def breakthrough(self):
		self.dailyMissionCommonMethod("breakthrough", 355, 355)

	def	treasureRefiningStone(self):
		self.dailyMissionCommonMethod("treasureRefiningStone", 275, 705)

	def	weaponRefiningStone(self):
		self.dailyMissionCommonMethod("weaponRefiningStone", 955, 800)

	# --------------------------------
	# 2.4.6.7

	def heroExp(self):
		self.dailyMissionCommonMethod("heroExp", 949, 370)

	def	treasureExp(self):
		self.dailyMissionCommonMethod("treasureExp", 1385, 572)

	def	spiritWeaponLvlupStone(self):
		self.dailyMissionCommonMethod("spiritWeaponLvlupStone", 1707, 721)

	# --------------------------------
	# Always
	def	gold(self):
		self.dailyMissionCommonMethod("gold", 1684, 361)

	def dailyMissionCommonMethod(self, missionType, locationx, locationy):
		print("Excute " + missionType)
		# Enter
		click(int(locationx), int(locationy))
		sleep(1.5)

		for i in range(1, 3):
			# Fight Middle one
			print("Fight " + missionType +" for the " + str(i) + "th times")
			click(900, 785)
			sleep(6)

			# 跳过

			click(1826, 1035)
			sleep(3)

			click(1826, 1035)
			sleep(1)

		# back
		print(missionType + " END")
		for i in range(1, 5):
			click(1826, 1035)

		sleep(2)

	def applyAuto3Guo_guan_zhan_jiang(self):
		#在adventure界面
		self.enter3Guo_guan_zhan_jiang()
		# 点完扫荡就回去
		click(1650, 975)
		sleep(10)
		click(1650, 975)
		back()
		sleep(2)

	def applyAuto4Land(self):
		# enter adventure-land
		print("enter Land")
		self.enter4Land()
		global presentAccountNumber
		PAN = presentAccountNumber

		LandAccountTimesDic = {1:3, 2:4, 3:4, 4:3, 5:4, 6:4, 7:4, 8:4, 9:3, 10:4 ,
				 11:4, 12:3, 13:4, 14:3, 15:3, 16:3, 17:3, 18:3, 19:4, 20:3}
		print("Now Excute collect_xth_position_Land 领地巡逻")
		for i in range(1, LandAccountTimesDic[PAN] + 1):
			self.collect_xth_position_Land(i)
		back()
		sleep(2)



	def collect_xth_position_Land(self, pos):
		
		# 指定位置
		# x : 1-徐州 2-豫州 3-荆州 4-青州 5-幽州 6-兖州
		LandPositionDic = { 1 : (486, 342), 2 : (318, 777),
							 3 : (870, 887), 4 : (983, 547), 
							 5 : (1426, 418), 6 : (1619, 809)}
		pos_x = LandPositionDic[pos][0]
		pos_y = LandPositionDic[pos][1]

		# collect part
		# click pos
		print("collect part")
		click(pos_x, pos_y)
		sleep(2)

		# click complete
		click(1380, 901)
		sleep(2)

		click(1380, 901)
		sleep(1)

		# arrange part
		# click pos
		print("arrange part")
		click(pos_x, pos_y)
		sleep(2)

		click(587, 622)
		sleep(2)

		# choose
		click(824, 305)
		sleep(1)

		# choose time
		click(1660, 786)
		sleep(1)

		# confirm
		click(1380, 901)
		sleep(1.5)
		#confirm again
		click(1169, 730)
		sleep(2)

		# back
		click(1710, 132)
		sleep(2)
'''
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

def main():
	print(deviceFlag)
	
	ADC.main(deviceFlag)

if __name__ == '__main__':
	main()


