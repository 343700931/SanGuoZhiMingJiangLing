import os
import subprocess
import datetime
import time
'''

该脚本专门用于刷三国志名将令的副本，要求为每天第一次打开游戏时执行（为了保证体力>50）

'''

devices = 0 #devices = 0 # 0 - Mobile ; 1 - Simulator

isUsingScale = True
blank = " "
xscale = 1
yscale = 1 

NO = 26

if isUsingScale:
	scale = 600 / 1920



presentAccount = False

def connect():
	global devices
	if not isUsingScale:
		os.system("adb connect 127.0.0.1:62001")
		noResponse = "unable" in subprocess.check_output("adb connect 127.0.0.1:62001").decode("utf-8")
		if not noResponse:
			devices = 1
		print("devices is ", devices)
	else:
		os.system("adb connect 127.0.0.1:620" + str(NO))
		noResponse = "unable" in subprocess.check_output("adb connect 127.0.0.1:62001").decode("utf-8")
		if not noResponse:
			devices = 2
		print("devices is ", devices)

def sleep(t):
	time.sleep(t)

def click(x, y):
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input tap " + str(x) + blank + str(y))
	if devices == 2:
		os.system("adb -s 127.0.0.1:620" + str(NO) + " shell input tap " + str(scale * x) + blank + str(scale * y + 57))
		print("xclick:", scale * x, ", yclick:", scale * y + 57)


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
	sleep(30)

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
	sleep(20)

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
	click(1482, 170)
	sleep(4)

	# Dinner
	click(142, 561)
	sleep(1)

	# Get dinner
	for i in range(1,4):
		click(1161, 675)
		sleep(0.3)

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
		# choose_by_x_axis(1183)
		choose_by_x_axis(1375)
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

	chooseEnemy(3)
	fight()
	sleep(5)

	# 一键宝箱
	click(968, 905)
	sleep(2)
	print("点跳过")
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
	click(78, 277)
	sleep(2)

	# 商城
	# buy blue one
	click(931, 433)
	sleep(2)
	click(1230, 547)
	sleep(1)
	click(1161, 810)
	sleep(2)

	# buy pink one
	click(1704, 429)
	sleep(2)
	click(1230, 547)
	sleep(1)
	click(1161, 810)
	sleep(2)

	# 竞技商店
	click(200, 550)
	sleep(3)

	click(943, 431)
	sleep(0.5)

	# 装备商店
	click(200, 687)
	sleep(3)

	# buy yellow stone
	click(931, 433)
	sleep(2)
	click(1230, 547)
	sleep(1)
	click(1161, 810)
	sleep(2)

	# 军团商店
	click(200, 960)
	sleep(3)

	click(931, 433)
	sleep(2)

	click(1704, 429)
	sleep(2)

	# END
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
	click(1482, 170)
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

	# Third 聚宝盆
	click(200, 687)
	sleep(2)

	click(1660, 907)
	sleep(0.5)
	click(1660, 907)
	sleep(0.5)

	back()
	sleep(4)

class Adventure(object):
	"""docstring for Adventure"""
	def __init__(self):
		super(Adventure, self).__init__()
		def enterAdventure(self):
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
		if int(time.strftime("%w")) in [1, 3, 5, 7]:
			# 武将经验、宝物经验、神兵进阶、银两
			heroExp()

			treasureExp()

			spiritWeaponLvlupStone()

		if int(time.strftime("%w")) in [2, 4, 6, 7]:
			# 突破丹、宝物精炼石、装备精炼石
			breakthrough()

			treasureRefiningStone()

			weaponRefiningStone()

			gold()

	def heroExp(self):
		pass

	def	treasureExp(self):
		pass

	def	spiritWeaponLvlupStone(self):
		pass

	def breakthrough(self):
		pass

	def	treasureRefiningStone(self):
		pass

	def	weaponRefiningStone(self):
		pass

	def	gold(self):
		pass

	def applyAuto3Guo_guan_zhan_jiang(self):
		#在adventure界面
		self.enter3Guo_guan_zhan_jiang()
		# 点完扫荡就回去
		click(1650, 975)
		sleep(10)
		click(1650, 975)
		back()
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

def autoDailyBonus():
	# Once a day
	autoShop()
	autoFuli()
	autoGuo_guan_zhan_jiang()

def autoCollectRedPiecesForOneTime():
	# Enter 活动
	click(1807, 168)
	sleep(4)

	# 军团活跃点多几次
	# for i in range(1, 4):
	# 	click(245, 375)
	# 	sleep(0.5)

	# collect
	for i in range(1, 4):
		click(1613, 520)
		sleep(0.2)

		click(1613, 800)
		sleep(0.2)

	# back
	click(1845, 131)
	sleep(4)

def autoCollectRedPieces():
	autoCollectRedPiecesForOneTime()
	autoCollectRedPiecesForOneTime()

def autoInvoke(acc):
	if acc == 1:
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
	click(1803, 338)
	sleep(4)

	# 如果中午打完boss，就是完成10个任务
	for i in range(1, 9):
		click(1696, 560)
		sleep(5)

	back()
	sleep(4)


def main():
	connect()

	# choose_by_x_axis(1541)
	# choose_by_x_axis(1228)
	# choose_by_x_axis(350)
	# x, y = countPositionXandY()
	# print(x, y)
	# switchAccount(2)
	# autoDinner()
	# autoMine()

	# for i in range(1, 4):
	# 	autoNormalBattle() 


	# autoMiddleBattle()
	
	# autoClubSignIn() 
	# autoDailyCounterpartRun()
	# autoDailyBonus()

	# autoGuo_guan_zhan_jiang()
	# autoInvoke()
	# print("自动好友送精力")
	# autoFriends()

	# print("自动收邮件")
	# autoCollectEmail()
	
	# print("自动完成任务，一天一次，晚上7点后完成")
	# autoFinishMission()


# '''
	for i in range(2, 21):
		# if i in []:
		# 	print(i, " skip")
		# 	continue
		switchAccount(i)
	# #	--------------------------------
	# #	--------------------------------

	# # 	***********
	# # 	 一天多次
	# # 	***********

		print("开始自动宴会")
		autoDinner()

		print("开始自动收矿")
		autoMine()

		# print("autoInvoke")
		# autoInvoke(i)

# '''
'''
		## --------------------------------
		## --------------------------------

		## 一天一次

		print("开始自动军团祭祀")
		autoClubSignIn()

		print("开始每日自动购买商店和收福利")
		autoDailyBonus()

		print("开始每日自动过关斩将")
		autoGuo_guan_zhan_jiang()

		print("自动好友送精力")
		# autoFriends()

		print("自动收邮件")
		autoCollectEmail()
'''

'''
		# print("开始自动每日副本")
		# if i == 1 or i == 7 or i == 9 or i == 10 or i == 11 or i ==12 or i ==14 or i == 15 or i == 16 or i == 17 or i == 18:
		#  	print(i, " skip")
		#  	continue
		# autoDailyCounterpartRun()


		# print("自动完成任务，一天一次，晚上7点后完成")
		# if i in [1, ]:
		# 	print(i, " skip")
		# 	continue
		# autoFinishMission()

		## !!!  晚上24点前用！否则刷新！  !!!
		# print("晚上7点后用的，自动收集红色碎片")
		# autoCollectRedPieces()

		# print("晚上7点后用的，自动收集军团的物资")
		# autoCollectClubBonus()

		## --------------------------------
		## --------------------------------
'''

if __name__ == '__main__':
	main()


