import os
import subprocess
import datetime
import time
from threading import Thread, Lock
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

'''

该脚本专门用于刷三国志名将令的副本，要求为每天第一次打开游戏时执行（为了保证体力>50）

'''
deviceFlag = 1 # 1 - 01 , 2 - 25 , 3 - 27

NOList = ["01", "25", "27"]

NO = NOList[deviceFlag - 1]

presentAccountNumber = 0 # 当前切到了哪个号， 0 表示有问题

# @Global variable

# 记录每天已经完成任务的号
account_done_mission = []

# lvl no less than 70 # Email and friends diff
moreThan70 = [1, 6, 5, 3]

# lvl no less than 65
# TODO
autoInvokeList = [1, 2, 3, 4, 5, 6]

# lvl no less than 58
clubShopMemberList = [1, 2, 3, 4, 5, 6, 7, 8]

connectTimes = 0

def setNO(num):
	print("setNO")
	global NO
	NO = NOList[num - 1]
	print('Present NO is', NO)

def getNO():
	global NO
	return NO

devices = 0 #devices = 0 # 0 - Mobile ; 1 - Simulator

isUsingScale = True
blank = " "
scale = 1

if isUsingScale:
	scale = 600 / 1920

presentAccount = False

def connect(no = 26):
	print(no)
	global devices
	global connectTimes
	'''
	# if not isUsingScale:
	# 	os.system("adb connect 127.0.0.1:62001")
	# 	noResponse = "unable" in subprocess.check_output("adb connect 127.0.0.1:62001").decode("utf-8")
	# 	if not noResponse:
	# 		devices = 1
	# 	print("devices is ", devices)
	# else:
	'''
	print("adb connect 127.0.0.1:620" + str(no))
	os.system("adb connect 127.0.0.1:620" + str(no))
	noResponse = "unable" in subprocess.check_output("adb connect 127.0.0.1:620" + str(no)).decode("utf-8")
	if not noResponse:
		devices = 2
	
	connectTimes += 1
	print("devices is ", devices, "\nconnectTimes is ", connectTimes)

	if devices == 0:
		if connectTimes <= 3:
			print("devices is ", devices, ", Reconnecting...")
			sleep(2)
			connect(no)
		else:
			print("connect too many times, but all fail.")

def sleep(t):
	time.sleep(t)

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

class AccountNumberException(Exception):
	"""docstring for AccountNumberException"""
	def __init__(self):
		super(AccountNumberException, self).__init__()
		print("presentAccountNumber should not be equal to ", presentAccountNumber)

def back():
	click(105, 35)

def skipPlot():
	print("狂点跳剧情")
	for i in range(1, 6):
		click(1815, 1019)
		sleep(0.2)

def fight():
	print("click 挑战")
	click(1484, 867)
	sleep(8)
	skipPlot()

	print("点跳过")
	click(1795, 1042)
	sleep(0.2)
	skipPlot()

	sleep(3)

def adbInput(string):
	if devices == 1:
		os.system("adb -s 127.0.0.1:62021 shell input " + string)
	if devices == 2:
		os.system("adb -s 127.0.0.1:620" + str(NO) + " shell input " + string)

def switchAccount(x):
	global presentAccount
	global presentAccountNumber
	presentAccountNumber = x
	if x == 1:
		presentAccount = True
	else:
		presentAccount = False
	accountNum = x + 30
	print("*************************")
	print("Now change account to No." + str(x))
	print("*************************")
	print("Click 头像")
	click(83, 83)
	sleep(4)

	print("click change account")
	click(392, 922)
	sleep(2)

	print("click confirm")
	click(1155, 726)
	sleep(22)

	print("点公告")
	click(961, 927)
	sleep(2)

	print("进入选项框")
	click(1004, 439)
	sleep(1)

	print("del twice")
	adbInput("keyevent 67")
	sleep(0.3)
	adbInput("keyevent 67")
	sleep(0.3)
	print("输入新的No.")
	adbInput("text " + str(accountNum))

	print("Click login")
	click(962, 667)
	sleep(3)

	print("点垃圾提示框")
	click(1116, 813)
	sleep(1)

	print("有时要再点一次登录")
	click(962, 667)
	sleep(3)

	print("登录游戏")
	click(956, 919)
	sleep(12)

def autoDailyCounterpartRun():
	sleep(2)
	print("Enter 战役")
	click(1794, 980)
	sleep(4)

	print("选择名将副本")
	click(1482, 43)
	sleep(2)

	print("点进去")
	click(1006, 431)
	sleep(0.3)
	click(1006, 822)
	sleep(4)



	# re-click to ensure that the plot has ended
	skipPlot()

	# -------  First one start ---------
	print("fight the first enemy")
	print("choose")
	click(636, 814)
	sleep(0.3)
	click(784, 601)
	sleep(0.3)
	click(718, 503)
	sleep(0.3)
	click(648, 606)

	sleep(4.5)

	fight()

	skipPlot()
	print("Fight 1st end")
	# -------  First one end ---------

	# ------- 2 ~ 4 --------
	for i in range(2, 5):
		print("choose")
		click(970, 430)
		sleep(0.3)
		click(970, 574)
		sleep(0.3)
		click(970, 813)

		sleep(4.5)
		fight()

		click(1285, 599)
		sleep(1)
		click(1285, 599)
		sleep(3)

		print("Fight ", str(i), "st End")
	# ------ 2 ~ 4 End ------

	# ------ Last one --------- 

	print("the last enemy")
	print("choose")
	choose_by_x_axis(1514)
	choose_by_x_axis(1364)
	choose_by_x_axis(1205)

	sleep(6)
	fight()

	skipPlot()
	sleep(5)

	print("Fight last End")
	# ------ Last one end --------- 

	print("拿宝箱")
	click(1832, 216)
	sleep(2)

	click(967, 821)
	sleep(2)

	click(967, 821)
	sleep(1)

	skipPlot()

	print("Back to main scene")
	back()
	sleep(4)
	back()
	sleep(8)

def autoDinner():
	# 福利
	# click(1482, 170) # 如果有类似元旦活动的时候，用这个
	click(1647, 170)
	sleep(4)

	# Dinner
	click(200, 561)
	sleep(1)

	# Get dinner
	for i in range(1,4):
		click(1161, 675)


	# back
	back()
	sleep(5)

def autoMine():
	print("Enter mine")
	click(1643, 790)
	sleep(2)
	click(1040, 500)
	sleep(1)
	back()
	sleep(3)

def choose_by_x_axis(x):
	a = 380
	b = 495
	c = 535
	d = 646
	e = 786
	for i in [a, b, c, d, e]:
		click(x, i)
		sleep(0.2)

def chooseEnemy(x):
	if x == 0:
		print("选择第一个敌人")
		choose_by_x_axis(341)
	if x == 1:
		print("选择第2个敌人")
		# choose_by_x_axis(638)
		# choose_by_x_axis(797)
		a = 380
		b = 495
		c = 535
		d = 686
		for i in [a, b, c, d]:
			click(628, i)
			sleep(0.2)

		choose_by_x_axis(797)
	if x == 2:
		print("选择中间的敌人")
		choose_by_x_axis(961)
	if x == 3:
		print("选择最后一个敌人")
		choose_by_x_axis(1200)
		choose_by_x_axis(1375)
		choose_by_x_axis(1490)
	sleep(3)

def enterBattle():
	print("Enter 战役")
	click(1794, 980)
	sleep(4)
	choose_by_x_axis(970)
	sleep(5)

def autoNormalBattle():

	enterBattle()

	chooseEnemy(0)
	fight()
	chooseEnemy(1)
	fight()
	for i in range(1, 9):
		chooseEnemy(2)
		fight()
		print("collect 一键宝箱")
		click(968, 905)
		sleep(2)

	chooseEnemy(3)
	fight()
	sleep(15)

	# 一键宝箱
	print("collect 一键宝箱")
	click(968, 905)
	sleep(2)
	click(1795, 1042)
	sleep(0.2)
	sleep(5)

def autoMiddleBattle():
	for i in range(1, 9):
		chooseEnemy(2)
		fight()

	chooseEnemy(3)
	fight()

def autoClubSignIn():
	isBigAccount = presentAccount

	# Enter club
	click(1431, 993)
	sleep(3)

	# Enter SignIn
	click(1561, 703)
	sleep(2)

	if isBigAccount == True:
		click(461, 861)
	else:
		click(950, 861)

	sleep(2)

	# Exit
	click(1709, 136)
	sleep(2)

	back()
	sleep(4)



def autoShop():
	def buyFirstPlace():
		# buy blue one
		click(931, 433)
		sleep(2)
		click(1230, 547)
		sleep(1)
		click(1161, 810)
		sleep(2)
	def buySecondPlace():
		# buy pink one
		click(1704, 429)
		sleep(2)
		click(1230, 547)
		sleep(1)
		click(1161, 810)
		sleep(2)

	# -------
	#  start
	# -------

	# Enter Shop
	click(78, 277)
	sleep(2)

	# 商城
	# buy blue one
	buyFirstPlace()

	# buy pink one
	buySecondPlace()

	# 竞技商店
	click(200, 550)
	sleep(3)

	click(943, 431)
	sleep(0.5)

	# 装备商店
	click(200, 687)
	sleep(3)

	# buy yellow stone
	buyFirstPlace()

	# 军团商店
	global presentAccountNumber
	if presentAccountNumber == 0:
		raise AccountNumberException()

	if presentAccountNumber in clubShopMemberList:
		# enter 军团商店
		click(200, 960)
		sleep(3)

		swipe(1077, 700, 1077, 300)
		sleep(0.5)
		swipe(1077, 700, 1077, 300)
		sleep(0.5)
		# 确保退出迷之窗口
		click(1058, 129)
		sleep(0.5)
		click(1058, 129)
		sleep(0.5)

		click(929, 360)
		sleep(0.5)
		click(1713, 360)
		sleep(0.5)

	else:
		click(200, 960)
		sleep(3)

		click(931, 433)
		sleep(2)

		click(1704, 429)
		sleep(2)

	# END
	click(601, 60)
	sleep(0.5)
	click(601, 60)
	sleep(0.5)

	back()
	sleep(4)

def countDays():
	a = datetime.datetime(2018, 12, 31)
	b = datetime.datetime.now()
	return (b-a).days

def countPositionXandY():
	days = countDays()
	x_count = days % 7
	y_count = days // 7 + 1
	if x_count == 0:
		x_count = 7
		y_count -= 1
	x = (x_count - 1) * 225 + 405
	y = (y_count - 1) * 210 + 345
	# test
	# x = x_count
	# y = y_count
	return x, y

def autoFuli():
	'''
	**************************
	#for lvl no less than 50 !
	**************************
	'''

	# 福利
	# click(1482, 170) # 如果有类似元旦活动的时候，用这个
	click(1647, 170)
	sleep(4)



	# First, sign
	click(200, 276)
	sleep(2)
	x, y = countPositionXandY()
	click(x, y)
	sleep(2)


	# 确保退出迷之窗口
	click(1058, 129)
	sleep(0.5)
	click(1058, 129)
	sleep(0.5)

	print("每日签到 END")

	# Second 五谷丰登
	click(200, 407)
	sleep(2)

	click(514, 330)
	sleep(2)

	click(853, 606)
	sleep(2)

	click(514, 606)
	sleep(2)

	# 领取
	click(853, 940)
	sleep(3)
	print("五谷丰登 END")

	# Third 聚宝盆
	click(230, 687)
	sleep(2)

	click(1660, 907)
	sleep(0.5)
	click(1660, 907)
	sleep(0.5)
	print("聚宝盆 END")

	# Forth Resource Recycle
	print("Resource Recycle")
	swipe(194, 699, 194, 355)
	sleep(1)
	swipe(194, 699, 194, 355)
	sleep(1)

	# Click Resource Recycle
	click(200, 938)
	sleep(1)

	click(692, 309)
	sleep(1.5)

	for i in range(1, 20):
		click(947, 509)
		sleep(0.2)

	print("Resource Recycle END")

	print("AutoFuli END")
	back()
	sleep(4)

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

		LandAccountTimesDic = {1:6, 2:5, 3:5, 4:4, 5:5, 6:5, 7:4, 8:4,
		 9:3, 10:4, 11:4, 12:3, 13:4, 14:3, 15:4, 16:3, 
		 17:3, 18:3, 19:4, 20:3}
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

def autoGuo_guan_zhan_jiang():
	adventureObject = Adventure()

	# 冒险
	# 过关斩将
	# 三星扫荡 & 等待
	adventureObject.applyAuto3Guo_guan_zhan_jiang()

	# 回去
	back()
	sleep(4)

def autoDailyMission():
	adventureObject = Adventure()

	# 冒险
	# 每日副本
	# 扫荡
	adventureObject.applyAuto2DailyMission()

	# 回去
	back()
	sleep(4)

def autoArena():
	adventureObject = Adventure()

	# 冒险
	# 竞技场
	# 扫荡
	adventureObject.applyAuto1Arena()

	# 回去
	back()
	sleep(4)

def autoLand():
	adventureObject = Adventure()
	# 冒险
	# 领地巡逻
	adventureObject.applyAuto4Land()

	# 回去
	back()
	sleep(4)


def autoDailyBonus():
	# Once a day
	autoShop()
	autoFuli()
	# In adventure
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
	print("        Now auto Adventure")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
	autoGuo_guan_zhan_jiang()
	autoArena()
	autoDailyMission()

	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
	print("        auto Adventure END")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

def autoCollectRedPiecesForOneTime():
	# Enter 活动
	# click(1650, 168) # 如果有类似元旦活动，点这个
	click(1815, 168)
	sleep(4)

	# 军团活跃点多几次
	# Reference
	# 1 - 5 行 Y 轴 : 230 375 515 655 800
	y1, y2, y3, y4, y5 = 230, 375, 515, 655, 800

	for i in range(1, 4):
		click(245, y1)
		sleep(0.5)

	# collect
	for i in range(1, 4):
		click(1613, 520)
		sleep(0.2)

		click(1613, 800)
		sleep(0.2)

	# back
	click(1845, 131)
	sleep(4)

def yuandan():
	click(1805, 170)
	sleep(2)

	click(888, 206)
	sleep(1)

	# Daily Bonus
	click(1644, 443)
	sleep(2)

	click(307, 665)
	sleep(2)

	for i in range(1, 8):
		click(1644, 443)
		sleep(0.3)

	# Exit
	click(1765, 121)
	sleep(2)

def autoCollectRedPieces():
	autoCollectRedPiecesForOneTime()
	autoCollectRedPiecesForOneTime()
	# yuandan()

def autoInvoke(acc):
	global autoInvokeList
	if acc in autoInvokeList:
		click(954, 1002)
		sleep(2)
	else:
		click(834, 985)
		sleep(2)

	click(1061, 877)
	sleep(5)
	click(1061, 877)
	sleep(1)
	click(482, 870)
	sleep(3)

	click(482, 870)
	sleep(5)
	click(482, 870)
	sleep(1)
	click(482, 870)
	sleep(0.2)

	back()
	sleep(4)

def autoCollectClubBonus():
	# Enter club
	click(1431, 993)
	sleep(3)

	# Enter SignIn
	click(1561, 703)
	sleep(2)

	# Collect
	click(697, 219)
	sleep(0.2)
	click(906, 219)
	sleep(0.2)
	click(697, 219)
	sleep(0.2)
	click(906, 219)
	sleep(0.2)

	# Exit
	click(1709, 136)
	sleep(2)

	# Enter Club House
	click(1580, 265)
	sleep(2)

	# Collect
	click(1037, 367)
	sleep(0.2)
	click(1254, 364)
	sleep(0.2)
	click(1037, 367)
	sleep(0.2)
	click(1254, 364)
	sleep(0.2)

	# Exit
	click(1709, 136)
	sleep(2)

	back()
	sleep(4)

def autoCollectEmail():
	if presentAccountNumber in moreThan70:
		return
	# 更多
	click(98, 428)
	sleep(2)

	click(1053, 496)
	sleep(3)

	# Collect
	click(327, 933)
	sleep(0.5)
	# Delete
	click(650, 931)
	sleep(0.5)

	# Again
	click(327, 933)
	sleep(0.5)
	click(650, 931)
	sleep(0.5)

	# Close
	back()
	sleep(4)

def autoFriends():
	if presentAccountNumber in moreThan70:
		return
	# 更多
	click(98, 428)
	sleep(2)

	# Friends
	click(303, 650)
	sleep(3)

	# Collect
	click(148, 269)
	sleep(0.8)
	click(1711, 977)
	sleep(0.8)

	click(148, 530)
	sleep(0.8)
	click(1711, 977)
	sleep(0.8)

	# Exit
	back()
	sleep(4)

def autoFinishMission():
	# 任务这一行从右向左数，第一个为x1常规位置，第二个为x2
	x1, x2 = 1803, 1637
	click(x2, 330)
	sleep(4)

	# 如果中午打完boss，就是完成10个任务
	# 如果晚上，大部分都要到13
	for i in range(1, 12):
		click(1696, 560)
		sleep(5)

	# 如果中午打完boss，就是完成10个任务
	# 如果晚上，大部分都要到13
	def click_box(x):
		if x not in [1, 2, 3, 4, 5]:
			print("x is out of range")
			raise Exception 
		x1, x2, x3, x4, x5 = 714, 953, 1202, 1440, 1690
		x_list = [x1, x2, x3, x4, x5]
		# box
		for i in range(1, 4):
			click(x_list[x - 1], 270)
			sleep(0.5)
		sleep(5)
		# 退出迷之窗口
		for i in range(1, 6):
			click(482, 111)
			sleep(0.2)
		sleep(5)


	for x in range(1, 6):
		click_box(x)

	back()
	sleep(4)


def autoYouLi(i):
	# i : 1 - 上方 2 - 中下 3 - 下
	# WARNING 需要提前打开自动游历
	# 进入指定的游历区域，中垂线上
	x = 910
	y1, y2, y3 = 375, 645, 900 
	if i == 1:
		click(x, y1)
	elif i == 2:
		click(x, y2)
	else:
		click(x, y3)
	sleep(3)

	# 用丹
	click(1185, 36)
	sleep(2)
	# 7颗
	for i in range(1, 10):
		click(1145, 736)
		sleep(1)
	# Exit
	click(1700, 600)
	sleep(1)

	# 点击开始
	print('开始自动游历')
	click(1715, 960)

	sleep(80)

	# Exit
	click(1700, 600)
	sleep(1)

def zao(x, y):
	# 早
	for i in range(x, y):
		# if i in [3, 4,5,6]:
		# 	continue
		switchAccount(i)

		print("开始领地巡逻")
		# if i != 1:
		autoLand()

		print("开始自动收矿")
		autoMine()

		# autoDinner()

		print("autoInvoke")
		autoInvoke(i)

		print("开始自动军团祭祀")
		autoClubSignIn()

		print("开始每日自动购买商店和收福利")
		autoDailyBonus()

		print("自动好友送精力")
		autoFriends()

		print("自动收邮件")
		autoCollectEmail()

def wan(x, y):
	# 晚
	for i in range(x, y):
		switchAccount(i)

		print("开始自动宴会")
		autoDinner()

		print("开始自动收矿")
		autoMine()

		print("自动收邮件")
		autoCollectEmail()

		# !!!  晚上24点前用！否则刷新！  !!!
		print("晚上7点后用的，自动收集红色碎片")
		autoCollectRedPieces()

		print("晚上7点后用的，自动收集军团的物资")
		autoCollectClubBonus()

		print("自动完成任务，一天一次，晚上7点后完成")
		if i in account_done_mission:
			print(i, " skip")
			continue
		autoFinishMission()



def main(df):
	global NO 
	global deviceFlag
	deviceFlag = df
	# no = NO
	# sleep(1)
	print(deviceFlag)
	setNO(deviceFlag)
	connect(NO)
	xList = [1, 8, 16]
	x = xList[deviceFlag - 1]

	yList = [8, 16, 21]
	y = yList[deviceFlag - 1]


	# ---------------------------------
	# ------------TASK PART------------
	# ---------------------------------

	# 早
	# zao(x, y)

	# 晚
	# wan(x, y)

	# 临时
	# '''
	# switchAccount(1)
	# for i in range(1, 8):
	#  	autoNormalBattle() 
	# '''

	# 临时
	# '''
	for i in range(x, y):
		if i != 1:
			switchAccount(i)

		# autoDailyMission()

		print("开始自动宴会")
		autoDinner()
		autoInvoke(i)
	# '''
	# print("自动领地巡逻")
	# autoLand()

	# ---------------------------------
	# ------------TASK PART------------
	# ---------------------------------


	# autoArena()
	# autoDailyMission()
	# autoMine()
	# autoCollectEmail()
	# autoCollectRedPieces()



	# ------------------------------------------------
	'''
	# def multiRun():

	p = ProcessPoolExecutor(3)
	objs = []
	# l = [p.submit(task, i) for i in range(1, 4)]
	for i in range(3):
		obj = p.submit(task, i)  # 异步调用
		objs.append(obj)

	for obj in objs:
		print(obj.result())

	p.shutdown(wait = True)
	print('='*30)
	print('Auto End')

	'''
	# ------------------------------------------------

	'''
	pool = Pool(processes = 5)
	print('the test has started')
	pool.map(main, urls)
	pool.close()
	pool.join()
	'''

def task(i):
	if i == 1:
		print("hello")
	elif i == 2:
		print("Hi")
	else:
		print("Fuck")
	global deviceFlag
	deviceFlag = i
	yield deviceFlag
	print("deviceFlag is: ", deviceFlag)
	setNO(deviceFlag)
	print(getNO())
	for i in range(1, 4):
		sleep(2)
		print("deviceFlag is: ", deviceFlag)
	# connect(NO)

	xList = [1, 8, 16]
	x = xList[deviceFlag - 1]

	yList = [8, 16, 21]
	y = yList[deviceFlag - 1]

	zao(x, y)

	# wan(x, y)

if __name__ == '__main__':
	main(deviceFlag)


