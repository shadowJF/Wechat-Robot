from message_handler import *
from pydub import AudioSegment
import os
import itchat

class TextMessageHandler(MessageHandler):
	def handleMessage(self,msg,userid=None,text=None):
		if userid == None:
			userid = msg['FromUserName']
		user = itchat.search_friends(userName=userid)
		userid = user['RemarkName']
		if userid == "":
			userid = user["NickName"]
		if text == None:		
			text = msg['Text']
		result = self.callChatRobot(userid,text)
		return result

class VoiceMessageHandler(MessageHandler):
	def handleMessage(self,msg,userid=None,text=None):
		userid = msg['FromUserName']
		user = itchat.search_friends(userName=userid)
		userid = user['RemarkName']
		if userid == "":
			userid = user["NickName"]
		fileName = msg['FileName']
		newFileName = fileName + '.wav'
		msg['Text'](fileName)
		sound = AudioSegment.from_mp3(fileName)
		sound.export(newFileName, format="wav")
		file = open(newFileName,"rb")
		fileBytes = file.read()
		file.close()
		os.remove(fileName)
		os.remove(newFileName)
		result = self.callChatRobotVoice(userid,fileBytes)
		return result
				

