# -*- encoding=utf8 -*-
import time
import logging
import os
import subprocess
import re

devices = 0 # 0 - Mobile ; 1 - Simulator

flag = 1 # 1 - Seasonal ; 2 - Official

acc = 1 # 1 - Elite ; 2 - Just for BOSS

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

blank = " "
xshift = 120
flagxshift =  False
# 点击屏幕x,y坐标
def xshiftClick(x, y):
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input tap " + str(x + xshift) + blank + str(y))
	else:
		os.system("adb shell input tap " + str(x + xshift) + blank + str(y))

def click(x, y):
	global devices
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input tap " + str(x) + blank + str(y))
	else:
		os.system("adb shell input tap " + str(x) + blank + str(y))

	# clickObj = subprocess.Popen("adb shell input tap " + "x " + "y")
	# clickObj.wait()

# 滑动屏幕， 从(x,y)到(x,y)，经过的时间用step来表示
def swipe(startx, starty, stopx, stopy, steps):
	global devices
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input swipe " + str(startx) + blank + str(starty) 
			+ blank + str(stopx) + blank + str(stopy))
	else:
		os.system("adb shell input swipe " + str(startx) + blank + str(starty) 
		+ blank + str(stopx) + blank + str(stopy))

def text(tex):
	global devices
	if devices == 1:
		os.system("adb -s 127.0.0.1:62001 shell input text " + str(tex))
	else:
		os.system("adb shell input text " + str(tex))


def sleep(n):
	time.sleep(n)

# 左上角返回键
def back():
	click(64, 90)
	sleep(1)

# Yellow double cross swords -- Battle 
def fight(): 
	click(1513, 442)
	sleep(1)

def ok():
	click(962, 895)
	sleep(1)

def arrangeHeroesFormation():
	# Arrange Heroes
	for i in range(1, 7):
		click(180 + (i - 1) * 170, 955)
		sleep(0.1)
	# Arrange Monster
	click(1535, 244)
	sleep(1)

	swipe(913, 548, 689, 548 , 40)
	sleep(1)
	swipe(913, 548, 789, 548 , 40)
	sleep(4)
	click(893, 821)
	click(1747, 121)
	# Arrange Heroes and Monster END

def swipeLeftForSpining():
	swipe(448, 227, 478, 227, 30)
	sleep(1)
	swipe(448, 227, 478, 227, 30)
	sleep(1)
	global flagxshift
	flagxshift = True

def swipeRightFormSpining():
	swipe(478, 227, 448, 227, 30)
	sleep(1)
	swipe(478, 227, 448, 227, 30)
	sleep(1)
	global flagxshift
	flagxshift = False

xMarket = 448
x_Market = xMarket + 80
def swipeLeftForMarket():
	for i in range(1, 6):
		swipe(xMarket, 227, x_Market, 227, 30)
		sleep(0.4)

def swipeRightBackAfterMarketing():
	for i in range(1, 6):
		swipe(x_Market, 227, xMarket, 227, 300)	
		sleep(0.4)

def buyConfirm():
	click(1140, 657)
	sleep(0.2)
	click(955, 184)
	sleep(0.2)

'''
	# IMPORTANT

	STEP LIST

	# Step1: Battle profits.

	# Step2: Spinning.

	# Step3: Event raid

	# Step4: Island(Not worth the time.)

	# Step5: Friends

	# Step6: Guild

	# Step7: Gold

	# Step8: Market #Once A Day#

	# Step9: Arena #Once A Day#


   
''' 


def Step1(): # Step1: Enter Battle and gain profits.
	logger.info("Step1 Battle Profits")
	try:
		# Step1:Enter Battle and gain profits.
		xshiftClick(991, 515)
		sleep(1)

		# Gain Gold and Green Soul
		click(1706, 211)
		logger.info("Wait for a few second if there's lvlup animation")
		sleep(6)

		# Gain Battle Prize
		logger.info("Gain battle prize")
		click(1651, 660)
		sleep(1)
		click(1651, 660)


		ok()
		sleep(0.5)

		back()
		
		# Step1 END
	
	except Exception as e:
		raise e
	logger.info("Step1 End")
def Step2(): # Step2: Spinning. #Once A Day#
	logger.info("Step2 Spining")
	try:
		# Step2: Spinning.
		# Enter spining
		click(137, 748)
		sleep(0.5)

		# Choose normal spin
		click(714, 540)
		sleep(2)

		# First spin
		click(959, 434)
		sleep(7)

		# Once again
		click(1204, 940)
		sleep(7)

		click(717, 940)
		sleep(0.5)

		back()
		# Step2 END
	
	except Exception as e:
		raise e
def Step3(): # Step3: Event raid. #Once A Day#
	logger.info("Step3 EventRaid")
	try:
		# Step3: Event raid
		click(1827, 212)
		sleep(2)

		# START
		for i in range(1,4):
			xPoint = 0
			if i == 1:
				xPoint = 482
			if i == 2:
				xPoint = 955
			if i == 3:
				xPoint = 1448
			if xPoint == 0:
				raise ValueError("xPoint值异常")

			click(xPoint, 856)
			sleep(1)

			if flag == 1: # Seasonal
				click(1338, 815)
			if flag == 2: # Official
				logger.info("swipe for the " + str(i) + " time")
				swipe(1121, 871 , 1121, 805, 30)
				sleep(1)
				click(1343, 847)
				sleep(1)
				
				click(1343, 669)
				
			sleep(2)

			if i == 1:
				arrangeHeroesFormation()
			fight()
			click(1245, 893)
			sleep(1)
			ok()

			# Close
			click(1527, 180)
			sleep(2)
		
		click(1715, 115) # Close Event raid
		# Step3: Event raid END
	except Exception as e:
		raise e
def Step4(): # Step4: Island.(Not worth the time.)
	logger.info("Step4 Island")
	try:
		# Not worth the time.
		# Elite Only
		# Step4: Island
		if acc == 1:
			# Enter islan
			if flagxshift == True:
				xshiftClick(69, 224)
			else:
				click(69, 224)
			sleep(1)

			# Gain profits
			click(1048, 659)
			sleep(0.3)

			click(915, 789)
			sleep(0.3)

			click(1162, 746)
			sleep(0.3)

			click(584, 439)
			sleep(0.3)
		
			# Go to Expedition
			click(544, 790)
			sleep(2)
			
			# Smash
			click(1786, 952)
			sleep(1.5)
			
			# Yes
			click(1138, 659)
			sleep(1)
			
			arrangeHeroesFormation()
			
			
			fight()
			ok()
			
			back()
			back()
		# Island END
	
	except Exception as e:
		raise e
def Step5(): # Step5: Friends
	logger.info("Step5 Friends")
	try:
		# Step5: Friends
		click(68, 658)
		sleep(1)

		click(1299, 256)
		sleep(0.3)

		click(1602, 820)
		sleep(0.3)

		click(925, 873) # scout
		sleep(3)

		click(1602, 820)
		sleep(0.3)

		click(1537, 110) # close
		sleep(1)
		# Step5: Friends END
	
	except Exception as e:
		raise e
def Step6(): # Step6: Guild.
	logger.info("Step6 Guild")
	try:
		# Step6: Guild
		click(1316, 1001) # Enter Guild
		sleep(2)

		click(626, 512) # Sign
		sleep(1)

		if acc != 2: # Mill
			click(473, 933)
			sleep(2)

			click(403, 408) # Enter Mill
			sleep(3.5)

			click(954, 766) # click OK
			sleep(3)

			ok()

			click(1377, 257) # Get order
			sleep(1.5)

			click(615, 820)
			sleep(0.5)
			click(1088, 820)
			sleep(0.5)
			click(1496, 820)
			sleep(0.5)

			click(1583, 101) # Close
			sleep(1)

			click(403, 408) # Enter Mill
			sleep(1)

			click(615, 820)
			sleep(0.5)
			click(1088, 820)
			sleep(0.5)

			click(1583, 101) # Close
			sleep(1)

			back()

		back()
		# Step6: Guild END
		logger.info("Step6: Guild END")

	except Exception as e:
		raise e
def Step7(): # Step7: Gold.
	logger.info("Step7 Gold")
	try:
		# Step7: Gold
		click(903, 54)
		sleep(1)

		click(781, 738)
		sleep(0.5)

		click(401, 381)
		sleep(0.5)

		click(1579, 240)
		sleep(0.5)

		# Step7: Gold END
		logger.info("Step7: Gold END")
	except Exception as e:
		raise e
def Step8(): # Step8: Market #Once A Day#
	logger.info("Step8 Market")
	if acc == 1:
		swipeLeftForMarket()

		# Enter Market
		xshiftClick(362, 904)
		sleep(1)

		# Buy Arena Tickets
		click(1099, 951)
		sleep(0.2)
		buyConfirm()

		click(1378, 951)
		sleep(0.2)
		buyConfirm()
		
		# NextPage
		click(1680, 679)

		# 3星
		for i in range(1,5):
			click(533 + (i - 1) * (813 - 533), 697)
			sleep(0.2)
			buyConfirm()

		back()

		swipeRightBackAfterMarketing()
		logger.info("Step8 Market END")

def Step9(): # Step9: Arena #Once A Day#
	logger.info("Step9 Arena")
	# Enter Arena -> Crystal Crown League
	xshiftClick(1279, 696)
	sleep(1.5)
	
	click(1253, 854)
	sleep(1.5)

	
	for i in range(1, 4):
		logger.info("The " + str(i) + "th battle." )
		# Click Battle
		click(1524, 640)
		sleep(1.5)

		# Choose the last one
		click(1425, 853)
		sleep(1.5)
		
		if i == 1:
			arrangeHeroesFormation()
			
		fight()
		click(965, 516)
		sleep(0.3)
		ok()
		ok()
	back()
	logger.info("Step9 Arena END")
def Step10(): # Step10: Accumulate Quests' Profits # Second Time Only ONCE #
	logger.info("Step10 Quests")
	# Enter
	click(1834, 485)
	sleep(1)

	for i in range(1, 5):
		click(1422, 533)
		sleep(1.8)

	#Close Quests
	click(1594, 120)
	sleep(1)
	logger.info("Step10 Quests END")
def changeXiaohaoAccount(account): # Change account
	logger.info("Now change xiaohao account to: " + account)
	click(1836, 640)
	sleep(1)
	
	click(1405, 721)
	sleep(0.5)
	
	# E-mail Address
	click(1015, 429)
	sleep(1)
	
	realAccount = "once" + str(account) + "@xiaohao.com"
	text(realAccount)
	sleep(1)
	
	# Password
	click(1095, 583)
	sleep(1)
	
	password = "123456"
	text(password)
	sleep(1)
	
	# login
	click(1154, 743)
	sleep(8)
def changeEliteAccount(account): # Change Elite Account
	logger.info("Now change Elite account to: " + account)
	click(1836, 640)
	sleep(1)
	
	click(1405, 721)
	sleep(0.5)
	
	# E-mail Address
	click(1015, 429)
	sleep(1)
	
	realAccount = "34370093" + str(account) + "@qq.com"
	text(realAccount)
	sleep(1)
	
	# Password
	click(1095, 583)
	sleep(1)
	
	password = "28159700"
	text(password)
	sleep(1)
	
	# login
	click(1154, 743)
	sleep(8)
def xiaohaoFirstTime():
	global acc
	acc = 2
	
	for i in range(1, 21):
		logger.info("第" + str(i) + "个小号")
		changeXiaohaoAccount(str(i))
		Step1()
		Step5()
		Step6()
		Step7()
def xiaohaoSecondTime():
	global acc
	acc = 2
	
	for i in range(1, 21):
		logger.info("第" + str(i) + "个小号")
		changeXiaohaoAccount(str(i))
		Step7()
		Step5()
		Step1()
def eliteFirstTime():
	global acc
	global flag
	acc = 1
	flag = 2
	# Fix deviation
	swipeLeftForSpining()
	sleep(1)
	
	for i in range(2, 8):
		logger.info("第" + str(i) + "个Elite小号")
		changeEliteAccount(str(i))
		Step7()
		Step5()
		Step1()
		Step6()
		Step4()

		Step9() #FirstTimeOnly
		Step3() #FirstTimeOnly
		#Step2() #FirstTimeOnly 
		#Step8() #FirstTimeOnly Market (取消)
	swipeRightFormSpining()
def eliteSecondTime():
	global acc
	global flag
	acc = 1
	flag = 2
	# swipeLeftForSpining()
	sleep(1)
	
	for i in range(2,8):
		logger.info("第" + str(i) + "个Elite小号")
		changeEliteAccount(str(i))
		Step7()
		Step5()
		Step1()
		Step6()
		Step4()

		# Step10() # Once Task
	# swipeRightFormSpining()

def bossAccountAutoAdd(x):
	logger.info("Now add the bosses to MAIN account.")
	for i in range(len(x)):
		changeXiaohaoAccount(str(x[i]))

		# Go to Friends
		click(68, 658)
		sleep(1)

		click(1622, 497)
		sleep(0.2)

		click(817, 264)
		sleep(0.5)

		text("74894705")
		sleep(1)

		# Apply
		click(1291, 257)
		sleep(0.5)

		# close
		click(1537, 110)
		sleep(1)

def autoClaimBonuses():
	#Open mail box
	click(64, 527)
	sleep(1.5)

	#Claim all
	click(514, 193)
	sleep(1)

	#delete all
	click(805, 196)
	sleep(1)

	#confirm
	click(1136, 691)
	sleep(2)

	#close
	click(1636, 124)
	sleep(2)



if __name__ == '__main__':
	
	try:
		# Connection
		# logger.info("sleep a while")
		# sleep(60 * 10)
		# logger.info("sleep END")
		os.system("adb connect 127.0.0.1:62001")
		noResponse = "unable" in subprocess.check_output("adb connect 127.0.0.1:62001").decode("utf-8")
		if not noResponse:
			devices = 1
		print("devices is ", devices)

		# 打boss
		bosses = [12, 5, 10]
		# bossAccountAutoAdd(bosses)


		for i in range(len(bosses)):
			changeXiaohaoAccount(str(bosses[i]))
			Step5()

		# xiaohaoFirstTime()
		# eliteFirstTime()


		# xiaohaoSecondTime()
		# eliteSecondTime()
		# changeEliteAccount("3")
 
		# swipeLeftForSpining()
		#swipeRightFormSpining()

		# Step6()
		
			
		# changeXiaohaoAccount("16")
		# autoClaimBonuses()
		# Step1()
		changeEliteAccount("1")
		# changeEliteAccount("3")
	except Exception as e:
		raise e