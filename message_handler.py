import requests
import json
import random
from robot_config import *

class MessageHandler:

	__chatRobotApiUrl = robot_url

	def handleMessage(self,msg,userid=None,text=None):
		return msg

	def callChatRobot(self,userid,text):
		postJson = self.__getPostData(userid,text)
		headers = {'content-type': 'application/json'}
		try:
			r = requests.post(self.__chatRobotApiUrl, data=json.dumps(postJson), headers=headers).json()
			return self.handleRobotResult(r)
		except:
			return '机器人出错啦~'

	def callChatRobotVoice(self,userid,fileBytes):
		apiUrl = robot_voice_url + '&appcode=wechat_personal&tenantid=ublinker&msgtype=voice&deviceid=test&sessionid=test&userid='+userid
		try:
			r = requests.post(apiUrl,data=fileBytes).json()
			return self.handleRobotResult(r)
		except:
			return '机器人出错啦~'

	def __getPostData(self,userid,text):
		data = {"appcode" : "wechat_personal","tenantid" : "ublinker",
			"msgtype" : "text","deviceid" : "wechat_personal","sessionid" : ""}
		data['msg'] = text
		data['userid'] = userid
		return data

	def handleRobotResult(self,r):
		code = r['code']
		
		if code == 100000:
			return r['text']
		elif code == 200000:
			return r['text'] + "\n" + "详情请点击: " + r['url']
		elif code == 200001:
			return r['text'] + "\n" + "详情请点击：" + r['url'] + "\n" + "图片链接: " + r['image']
		elif code == 302000:
			result = r['text'] + "\n"
			dataList = r['list']
			for entry in dataList:
				result += entry['article'] + "\n"
				result += entry['source'] + "\n"
				result += entry['detailurl'] + "\n"
			return result
		elif code == 308000:
			result = r['text'] + "\n"
			dataList = r['list']
			for entry in dataList:
				result += entry['name'] + "\n"
				result += entry['info'] + "\n"
				result += entry['detailurl'] + "\n"
			return result 
		elif code == 110000:
			#result = "您是否要问: " + "\n"
			dataList = r['answers']
			randomAnswer = random.choice(dataList)
			result = randomAnswer['text']
			#for entry in dataList:
			#	result += entry['question'] + "\n"
			return result
		else:
			return r['text']
